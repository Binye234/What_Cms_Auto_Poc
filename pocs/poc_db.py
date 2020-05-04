# -*- coding: utf-8 -*-
from find_cms.cms_enum import *
from pocs import *


class poc_db:
    def __init__(self):
        self.data = {
            Cms_Enum.dedecms: {
                "dedecms版本探测": "dedecms_version_BaseVerify(self.cms_mode.url).run()",
                "dedecms download.php重定向漏洞": "dedecms_download_redirect_BaseVerify(self.cms_mode.url).run()",
                "dedecms trace爆路径漏洞": "dedecms_error_trace_disclosure_BaseVerify(self.cms_mode.url).run()",
                "dedecms recommend.php SQL注入": "dedecms_recommend_sqli_BaseVerify(self.cms_mode.url).run()",
                "dedecms search.php SQL注入漏洞": "dedecms_search_typeArr_sqli_BaseVerify(self.cms_mode.url).run()",
            },
            Cms_Enum.phpcms: {
                "phpcms authkey泄露": "phpcms_authkey_disclosure_BaseVerify(self.cms_mode.url).run()",
                "phpcms digg_add.php SQL注入": "phpcms_digg_add_sqli_BaseVerify(self.cms_mode.url).run()",
                "phpcms2008 flash_upload.php SQL注入": "phpcms_flash_upload_sqli_BaseVerify(self.cms_mode.url).run()",
                "phpcms2008 product.php 代码执行": "phpcms_product_code_exec_BaseVerify(self.cms_mode.url).run()",
                "phpcms v9 flash xss漏洞": "phpcms_v9_flash_xss_BaseVerify(self.cms_mode.url).run()",
                "phpcms v9.6.0 SQL注入": "phpcms_v96_sqli_BaseVerify(self.cms_mode.url).run()",
                "phpcms 9.6.1任意文件读取漏洞": "phpcms_v961_fileread_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.seacms: {
                "seacms 6.45 search.php order参数前台代码执行": "seacms_order_code_exec_BaseVerify(self.cms_mode.url).run()",
                "seacms search.php 代码执行": "seacms_search_code_exec_BaseVerify(self.cms_mode.url).run()",
                "seacms search.php 参数jq代码执行": "seacms_search_jq_code_exec_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.discuz: {
                "discuz X3 focus.swf flashxss漏洞": "discuz_focus_flashxss_BaseVerify(self.cms_mode.url).run()",
                "discuz论坛forum.php参数message SSRF漏洞": "discuz_forum_message_ssrf_BaseVerify(self.cms_mode.url).run()",
                "discuz问卷调查参数orderby注入漏洞": "discuz_plugin_ques_sqli_BaseVerify(self.cms_mode.url).run()",
                "discuz! X2.5 物理路径泄露漏洞": "discuz_x25_path_disclosure_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.acsoft: {
                "安财软件GetFile任意文件读取": "acsoft_GetFile_fileread_BaseVerify(self.cms_mode.url).run()",
                "安财软件GetFileContent任意文件读取": "acsoft_GetFileContent_fileread_BaseVerify(self.cms_mode.url).run()",
                "安财软件GetXMLList任意文件读取": "acsoft_GetXMLList_fileread_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.cmseasy: {
                "cmseasy header.php 报错注入": "cmseasy_header_detail_sqli_BaseVerify(self.cms_mode.url).run()"

            },
            Cms_Enum.dreamgallery: {
                "dreamgallery album.php SQL注入": "dreamgallery_album_id_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.ecshop: {
                "ecshop3.0 flow.php 参数order_id注入": "ecshop_flow_orderid_sqli_BaseVerify(self.cms_mode.url).run()",
                "ecshop uc.php参数code SQL注入": "ecshop_uc_code_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.eyou: {
                "亿邮Email Defender系统免登陆DBA注入": "eyou_admin_id_sqli_BaseVerify(self.cms_mode.url).run()",
                "亿邮邮件系统重置密码问题暴力破解": "eyou_resetpw_BaseVerify(self.cms_mode.url).run()",
                "亿邮mail5 user 参数kw SQL注入": "eyou_user_kw_sqli_BaseVerify(self.cms_mode.url).run()",
                "亿邮邮箱弱口令列表泄露": "eyou_weakpass_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.fastmeeting: {
                "好视通视频会议系统(fastmeeting)任意文件遍历": "fastmeeting_download_filedownload_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.finecms: {
                "FineCMS免费版文件上传漏洞": "finecms_uploadfile_BaseVerify(self.cms_mode.url).run()"

            },
            Cms_Enum.FoosunCms: {
                "Dotnetcms(风讯cms)SQL注入漏洞": "foosun_City_ajax_sqli_BaseVerify(self.cms_mode.url).run()"

            },
            Cms_Enum.fsmcms: {
                "FSMCMS columninfo.jsp文件参数ColumnID SQL注入": "fsmcms_columninfo_sqli_BaseVerify(self.cms_mode.url).run()",
                "fsmcms p_replydetail.jsp注入漏洞": "fsmcms_p_replydetail_sqli_BaseVerify(self.cms_mode.url).run()",
                "FSMCMS网站重装漏洞": "fsmcms_setup_reinstall_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.gowinsoft_jw: {
                "金窗教务系统存在多处SQL注射漏洞": "gowinsoft_jw_multi_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.hanweb: {
                "大汉downfile.jsp 任意文件下载": "hanweb_downfile_filedownload_BaseVerify(self.cms_mode.url).run()",
                "大汉版通JCMS数据库配置文件读取漏洞": "hanweb_readxml_fileread_BaseVerify(self.cms_mode.url).run()",
                "大汉VerfiyCodeServlet越权漏洞": "hanweb_VerifyCodeServlet_install_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.joomla: {
                "joomla组件com_docman本地文件包含": "joomla_com_docman_lfi_BaseVerify(self.cms_mode.url).run()",
                "joomla 3.7.0 core SQL注入": "joomla_index_list_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.kxmail: {
                "科信邮件系统login.server.php 时间盲注": "kxmail_login_server_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.libsys: {
                "汇文软件图书管理系统ajax_asyn_link.php任意文件读取": "libsys_ajax_asyn_link_fileread_BaseVerify(self.cms_mode.url).run()",
                "汇文软件图书管理系统ajax_asyn_link.old.php任意文件读取": "libsys_ajax_asyn_link_old_fileread_BaseVerify(self.cms_mode.url).run()",
                "汇文软件图书管理系统ajax_get_file.php任意文件读取": "libsys_ajax_get_file_fileread_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.metinfo: {
                "metinfo5.0 getpassword.php两处时间盲注漏洞": "metinfo_getpassword_sqli_BaseVerify(self.cms_mode.url).run()",
                "metinfo v5.3sql注入漏洞": "metinfo_login_check_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.pageadmin: {
                "PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码": "pageadmin_forge_viewstate_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.phpok: {
                "phpok api.php SQL注入漏洞": "phpok_api_param_sqli_BaseVerify(self.cms_mode.url).run()",
                "phpok remote_image getshell漏洞": "phpok_remote_image_getshell_BaseVerify(self.cms_mode.url).run()",
                "phpok res_action_control.php 任意文件下载(需要cookies文件)": "phpok_res_action_control_filedownload_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.piaoyou: {
                "票友票务系统int_order.aspx SQL注入": "piaoyou_int_order_sqli_BaseVerify(self.cms_mode.url).run()",
                "票友机票预订系统6处SQL注入": "piaoyou_multi_sqli_BaseVerify(self.cms_mode.url).run()",
                "票友票务系统通用sql注入": "piaoyou_newsview_list_BaseVerify(self.cms_mode.url).run()",
                "票友机票预订系统6处SQL注入2(绕过)": "piaoyou_six2_sqli_BaseVerify(self.cms_mode.url).run()",
                "票友机票预订系统6处SQL注入(绕过)": "piaoyou_six_sqli_BaseVerify(self.cms_mode.url).run()",
                "票友机票预订系统10处SQL注入": "piaoyou_ten_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.qibocms: {
                "qibocms news/js.php文件参数f_idSQL注入": "qibocms_js_f_id_sqli_BaseVerify(self.cms_mode.url).run()",
                "qibocms s.php文件参数fids SQL注入": "qibocms_s_fids_sqli_BaseVerify(self.cms_mode.url).run()",
                "qibo分类系统search.php 代码执行": "qibocms_search_code_exec_BaseVerify(self.cms_mode.url).run()",
                "qibocms知道系统SQL注入": "qibocms_search_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.shopex: {
                "shopex敏感信息泄露": "shopex_phpinfo_disclosure_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.shopnc: {
                "shopNC B2B版 index.php SQL注入": "shopnc_index_class_id_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.siteengine: {
                "SiteEngine 6.0 & 7.1 SQL注入漏洞": "siteengine_comments_module_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.siteserver: {
                "siteserver3.6.4 background_administrator.aspx注入": "siteserver_background_administrator_sqli_BaseVerify(self.cms_mode.url).run()",
                "siteserver3.6.4 background_keywordsFilting.aspx注入": "siteserver_background_keywordsFilting_sqli_BaseVerify(self.cms_mode.url).run()",
                "siteserver3.6.4 background_log.aspx注入": "siteserver_background_log_sqli_BaseVerify(self.cms_mode.url).run()",
                "siteserver3.6.4 background_taskLog.aspx注入": "siteserver_background_taskLog_sqli_BaseVerify(self.cms_mode.url).run()",
                "siteserver3.6.4 user.aspx注入": "siteserver_UserNameCollection_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.thinkphp: {
                "Onethink 参数category SQL注入": "onethink_category_sqli_BaseVerify(self.cms_mode.url).run()",
                "ThinkPHP 代码执行漏洞": "thinkphp_code_exec_BaseVerify(self.cms_mode.url).run()",
                "ThinkPHP V5代码执行漏洞": "thinkphp_v5_exec_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.thinksns: {
                "thinksns category模块代码执行": "thinksns_category_code_exec_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.typecho: {
                "typecho install.php反序列化命令执行": "typecho_install_code_exec_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.umail: {
                "umail物理路径泄露": "umail_physical_path_BaseVerify(self.cms_mode.url).run()",
                "umail_physical_path_BaseVerify": "umail_sessionid_access_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.urp: {
                "urp查询接口曝露": "urp_query_BaseVerify(self.cms_mode.url).run()",
                "URP越权查看任意学生课表、成绩(需登录)": "urp_query2_BaseVerify(self.cms_mode.url).run()",
                "URP综合教务系统任意文件读取": "urp_ReadJavaScriptServlet_fileread_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.weaver_oa: {
                "泛微OA 数据库配置泄露": "weaver_oa_db_disclosure_BaseVerify(self.cms_mode.url).run()",
                "泛微OA filedownaction SQL注入": "weaver_oa_download_sqli_BaseVerify(self.cms_mode.url).run()",
                "泛微OA downfile.php 任意文件下载漏洞": "weaver_oa_filedownload_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.wecenter: {
                "wecenter SQL注入": "wecenter_topic_id_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.wordpress: {
                "wordpress admin-ajax.php任意文件下载": "wordpress_admin_ajax_filedownload_BaseVerify(self.cms_mode.url).run()",
                "wordpress display-widgets插件后门漏洞": "wordpress_display_widgets_backdoor_BaseVerify(self.cms_mode.url).run()",
                "Wordpress AzonPop插件SQL注入": "wordpress_plugin_azonpop_sqli_BaseVerify(self.cms_mode.url).run()",
                "wordpress 插件mailpress远程代码执行": "wordpress_plugin_mailpress_rce_BaseVerify(self.cms_mode.url).run()",
                "wordpress 插件shortcode0.2.3 本地文件包含": "wordpress_plugin_ShortCode_lfi_BaseVerify(self.cms_mode.url).run()",
                "wordpress rest api权限失效导致内容注入": "wordpress_restapi_sqli_BaseVerify(self.cms_mode.url).run()",
                "wordpress插件跳转": "wordpress_url_redirect_BaseVerify(self.cms_mode.url).run()",
                "wordpress 插件WooCommerce PHP代码注入": "wordpress_woocommerce_code_exec_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.xplus: {
                "xplus npmaker 2003系统GETSHELL": "xplus_2003_getshell_BaseVerify(self.cms_mode.url).run()",
                "xplus通用注入": "xplus_mysql_mssql_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.zfsoft: {
                "正方教务系统数据库任意操纵": "zfsoft_database_control_BaseVerify(self.cms_mode.url).run()",
                "正方教务系统default3.aspx爆破页面": "zfsoft_default3_bruteforce_BaseVerify(self.cms_mode.url).run()",
                "正方教务系统services.asmx SQL注入": "zfsoft_service_stryhm_sqli_BaseVerify(self.cms_mode.url).run()"
            },
            Cms_Enum.zuitu: {
                "最土团购SQL注入": "zuitu_coupon_id_sqli_BaseVerify(self.cms_mode.url).run()"
            }

        }
