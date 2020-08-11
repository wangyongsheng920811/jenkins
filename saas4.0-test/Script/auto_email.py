#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import sys
import requests
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class Gitlaber(object):
    """调用gitlab api 获取代码仓库各种信息"""
    host = 'https://code.dding.net/api/v4'
    headers = {'PRIVATE-TOKEN': 'k1Ndc21hscMCnF7dyNfm'}
    pms_api = '487'
    cms_api = '488'
    pms_web = '493'
    cms_web = '494'
    pms_migrate = '441'
    test = '471'

    @classmethod
    def get_latest_merge(cls, project_id):
        path = '/projects/' + project_id + '/merge_requests?state=merged'
        params = {
            'per_page': '2',
            'page': '1'
        }
        res = requests.get(cls.host + path, params=params, headers=cls.headers)
        merge_infos = res.json()[0]
        return [merge_infos.get('description'), merge_infos.get('merge_commit_sha')]

    @classmethod
    def get_latest_commit(cls, project_id):
        path = '/projects/' + project_id + '/repository/commits/master'
        res = requests.get(cls.host + path, headers=cls.headers)
        return res.json().get('id')


class Emailer(object):
    """上线邮件模板"""
    @staticmethod
    def get_user_email(user_name):
        user_emails = {
            'wangyongsheng': 'wangyongsheng@dding.cn',
            'zhengdai': 'zhengdai@dding.cn',
            'liuyue': 'liuyue@dding.cn',
            'xingzhiyuan': 'xingzhiyuan@dding.cn',
            '刘一航': 'liuyihang@dding.cn',
            '胡涛': 'hutao@dding.cn',
            'huangsiyun': 'huangsiyun@dding.cn',
            '王玉龙': 'wangyulong@dding.cn',
            'wangyulong': 'wangyulong@dding.cn',
            'gaochugang': 'gaochugang@dding.cn',
            'wangweiwei': 'wangweiwei@dding.cn',
            'yeweihan': 'yeweihan@dding.cn',
            'zhouchong': 'zhouchong@dding.cn',
            'herui': 'herui01@dding.cn',
            '何锐': 'herui01@dding.cn',
            'chenminqi': 'chenminqi@dding.cn',
            'yangxiong': 'yangxiong@dding.cn',
            'qiuting': 'qiuting@dding.cn',
            'liudongdong': 'liudongdong@dding.cn',
            'leidongxing': 'leidongxing@dding.cn',
            'sunyakun': 'sunyakun@dding.cn',
            'yehaochang': 'yehaochang@dding.cn',
            '叶浩昌': 'yehaochang@dding.cn'
        }

        return user_emails.get(user_name)

    @staticmethod
    def send_email(user_name, pms_api_info='', cms_api_info='', pms_web_info='', cms_web_info='', pms_migrate_info=''):
        from_addr = 'wangyongsheng@dding.cn'
        password = 'Wxs-920925'
        # to_addr = ['huangsiyun@dding.cn', 'wangyulong@dding.cn', 'hutao@dding.cn', 'gaochugang@dding.cn', 'wangweiwei@dding.cn', 'yeweihan@dding.cn']
        to_addr = ['wangyongsheng@dding.cn']
        to_addr.append(Emailer.get_user_email(user_name))
        cc_addr = ['wangyongsheng@dding.cn']
        smtp_server = 'SMTP.alibaba.com'

        if pms_web_info == '':
            pms_web_table = ''
            pms_web_commit_table = ''
            pms_web_update_command = ''
        else:
            pms_web_table = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;saas4-web-pms:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + pms_web_info[0].replace('\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;') + '</div><br>'
            pms_web_commit_table = '''
                <tr>
                    <td>saas4-web-pms</td>
                    <td>master</td>
                    <td>''' + pms_web_info[1] + '''</td>
                    <td>git@code.dding.net:server/lease-platform/Web/saas4-web-pms.git</td>
                </tr>'''
            pms_web_update_command = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;saas4-web-pms: </b><ul><li>更新代码</li></ul></div>'

        if cms_web_info == '':
            cms_web_table = ''
            cms_web_commit_table = ''
            cms_web_update_command = ''
        else:
            cms_web_table = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;saas4-web-cms:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + cms_web_info[0].replace('\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;') + '</div><br>'
            cms_web_commit_table = '''
                <tr>
                    <td>saas4-web-cms</td>
                    <td>master</td>
                    <td>''' + cms_web_info[1] + '''</td>
                    <td>git@code.dding.net:server/lease-platform/Web/saas4-web-cms.git</td>
                </tr>'''
            cms_web_update_command = '''
                <div><b>&nbsp;&nbsp;&nbsp;&nbsp;saas4-web-cms: </b>
                    <ul>
                        <li>更新代码</li>
                        <li>npm install</li>
                        <li>npm run build</li>
                        <li>部署/dist目录到线上环境</li>
                    </ul>
                </div>'''

        if pms_api_info == '':
            pms_api_table = ''
            pms_api_commit_table = ''
            pms_api_update_command = ''
        else:
            pms_api_table = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;pms-api:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + pms_api_info[0].replace('\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;') + '</div><br>'
            pms_api_commit_table = '''
                <tr>
                    <td>pms-api</td>
                    <td>master</td>
                    <td>''' + pms_api_info[1] + '''</td>
                    <td>git@code.dding.net:server/lease-platform/pms-api.git</td>
                </tr>'''
            pms_api_update_command = '''
                <div><b>&nbsp;&nbsp;&nbsp;&nbsp;pms-api: </b>
                    <ul>
                        <li>数据库变更：无</li>
                        <li>配置文件变更：无</li>
                        <li>其他变更：无</li>
                        <li>更新代码</li>
                        <li>重新部署release/qypms-boot.jar</li>
                    </ul>
                </div>'''

        if cms_api_info == '':
            cms_api_table = ''
            cms_api_commit_table = ''
            cms_api_update_command = ''
        else:
            cms_api_table = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;cms-api:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + cms_api_info[0].replace('\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;') + '</div><br>'
            cms_api_commit_table = '''
                <tr>
                    <td>cms-api</td>
                    <td>master</td>
                    <td>''' + cms_api_info[1] + '''</td>
                    <td>git@code.dding.net:server/lease-platform/cms-api.git</td>
                </tr>'''
            cms_api_update_command = '''
                <div><b>&nbsp;&nbsp;&nbsp;&nbsp;cms-api: </b>
                    <ul>
                        <li>数据库变更：无</li>
                        <li>配置文件变更：无</li>
                        <li>其他变更：无</li>
                        <li>更新代码</li>
                        <li>重新部署release/qycms-boot.jar</li>
                    </ul>
                </div>'''

        if pms_migrate_info == '':
            pms_migrate_table = ''
            pms_migrate_commit_table = ''
            pms_migrate_update_command = ''
        else:
            pms_migrate_table = '<div><b>&nbsp;&nbsp;&nbsp;&nbsp;pms-migrate:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + pms_migrate_info[0].replace('\n', '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;') + '</div><br>'
            pms_migrate_commit_table = '''
                <tr>
                    <td>pms-migrate</td>
                    <td>master</td>
                    <td>''' + pms_migrate_info[1] + '''</td>
                    <td>git@code.dding.net:server/gongyu/pms-migrate.git</td>
                </tr>'''
            pms_migrate_update_command = '''
                <div><b>&nbsp;&nbsp;&nbsp;&nbsp;pms-migrate: </b>
                    <ul>
                        <li>数据库变更：无</li>
                        <li>配置文件变更：无</li>
                        <li>其他变更：无</li>
                        <li>更新代码</li>
                        <li>重新部署release/pms-migrate.jar</li>
                    </ul>
                </div>'''

        web_htmlstr = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Document</title>
            </head>
            <body>
                <h3>1. 影响功能及模块 </h3> {} {} {} {} {}
                <h3>2. 部署环境</h3>
                <table border cellspacing="0" cellpadding="10">
                    <thead>
                        <tr>
                            <th>项目</th>
                            <th>分支</th>
                            <th>commit</th>
                            <th>项目地址</th>
                        </tr>
                    </thead>
                    <tbody> {} {} {} {} {}
                    </tbody>
                </table>
                <br>
                <h3>3. 操作步骤 </h3>{} {} {} {} {}
            </body>
            </html>'''.format(pms_api_table, cms_api_table, pms_web_table, cms_web_table, pms_migrate_table, pms_api_commit_table, cms_api_commit_table, pms_web_commit_table, cms_web_commit_table, pms_migrate_commit_table, pms_api_update_command, cms_api_update_command, pms_web_update_command, cms_web_update_command, pms_migrate_update_command)

        msg = MIMEText(web_htmlstr, 'html', 'utf-8')
        msg['From'] = from_addr
        msg['To'] = ";".join(to_addr)
        msg['Cc'] = ";".join(cc_addr)
        msg['Subject'] = Header('上线申请模板', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 80)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr + cc_addr, msg.as_string())
        server.quit()


if __name__ == '__main__':
    args = sys.argv[:]
    pms_web_info = ''
    cms_web_info = ''
    pms_api_info = ''
    cms_api_info = ''
    pms_migrate_info = ''
    user_name = args[-1]

    if 'pms_api' in args:
        pms_api_info = Gitlaber.get_latest_merge(Gitlaber.pms_api)
        pms_api_info[1] = Gitlaber.get_latest_commit(Gitlaber.pms_api)
    if 'cms_api' in args:
        cms_api_info = Gitlaber.get_latest_merge(Gitlaber.cms_api)
        cms_api_info[1] = Gitlaber.get_latest_commit(Gitlaber.cms_api)
    if 'pms_web' in args:
        pms_web_info = Gitlaber.get_latest_merge(Gitlaber.pms_web)
    if 'cms_web' in args:
        cms_web_info = Gitlaber.get_latest_merge(Gitlaber.cms_web)
    if 'pms_migrate' in args:
        pms_migrate_info = Gitlaber.get_latest_merge(Gitlaber.pms_migrate)
        pms_migrate_info[1] = Gitlaber.get_latest_commit(Gitlaber.pms_migrate)
    Emailer.send_email(user_name, pms_api_info, cms_api_info, pms_web_info, cms_web_info, pms_migrate_info)
