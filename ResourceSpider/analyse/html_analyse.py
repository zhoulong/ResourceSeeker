#coding:utf8
'''
Created on 2012-8-10

@author: zhoulong0116
'''

from BeautifulSoup import BeautifulSoup

def analyse(html):
    soup = BeautifulSoup(html)
    _analyse_js(soup)
    _analyse_hyperlink(soup)
    
def _analyse_js(soup):
    return None

def _analyse_hyperlink(soup):
    link_list = soup.findAll('a')
    for link in link_list:
        if link.has_key('href'):
            print link['href']
            print link.text
        

if __name__ == '__main__':
    html = '''
<!DOCTYPE HTML PUBLIC "-//W3C//dtD HTML 4.01 Transitional//EN" "http://www.w3c.org/TR/1999/REC-html401-19991224/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Java开源中文分词类库分类列表</title>
<meta http-equiv=Content-Type content="text/html; charset=GBK">
<meta name="description" content="Java开源中文分词类库分类列表">
<meta name="keywords" content="Java开源中文分词类库分类列表">
<meta http-equiv="Content-Type" content="text/html; charset=GBK">
<link href="resource/opencs.css" type=text/css rel=stylesheet>
<link href="favicon.ico" type=/image/x-icon rel=icon>
<link href="favicon.ico" type=/image/x-icon rel="shortcut icon">
<script type="text/javascript" src="resource/openjs_itemlist.js"></script>
<script type="text/javascript" >

function $(element) {
  return document.getElementById(element);
}

function SideBarToggle() {
        if ('block' == $('sidebar').style.display || ''==$('sidebar').style.display) {
            $('sidebar').style.display = 'none';$('dicts').style.width = '730px';$('sidebarToggleImg').src = 'resource/left_onck2.gif';
            $('sidebarToggleImg').alt = '显示导航栏';
        } else {
            $('sidebar').style.display = 'block';$('dicts').style.width = '730px';$('sidebarToggleImg').src = 'resource/left_onck.gif';
            $('sidebarToggleImg').alt = '关闭导航栏';
        }
};



</script>
<STYLE>
#kw {
    PADDING-BOTTOM: 3px; MARGIN: 0px 6px 0px 20px; PADDING-LEFT: 1px; WIDTH: 391px; VERTICAL-ALIGN: middle;PADDING-RIGHT: 1px; FONT: 16px arial; PADDING-TOP: 3px
}

#su {
    LINE-HEIGHT: 24px; WIDTH: 100px; HEIGHT: 28px;VERTICAL-ALIGN: middle
}

#nv {
    MARGIN: 0px 0px 4px 50px; FONT-SIZE: 15px
}
</STYLE>
</head>
<BODY>
<div id=top style="WIdtH: 99%">
<div id=seah_list style="WIdtH: 99%">
<div class=logo>
<IMG  alt="OPEN开源大全" src="resource/logo.gif" style="cursor: hand;" onclick="window.location='/';" class = "corner iradius8 ishade75 ishadow33" border=0>
</div>
<div class=seah>
<div class=input_div>


</div>
</div>
</div>
<div class=line style="WIdtH: 99%"></div>
<script type="text/javascript"><!--
google_ad_client = "pub-7963911354665843";
/* 728x15, 创建于 11-5-30 */
google_ad_slot = "5341898719";
google_ad_width = 728;
google_ad_height = 15;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
<div id=Contents style="WIdtH: 99%">
<table cellSpacing=0 cellPadding=0 width=1100 border=0>
  <tbody>
  <tr>
    <td class=left id=sidebar vAlign=top align=left width=200px>
      <dl>
        <DT>栏目导航</DT>
        <DD><a href='http://www.open-open.com/ajax'>JS脚本大全</a></DD>
        <DD><a href='http://www.open-open.com/lib/'>OPEN经验库</a><img src="image/new.gif" alt='最新上线'/></DD>        
            <DD><a href='http://www.open-open.com/doc/'>OPEN文档</a></DD>
         <DD><a href='http://www.open-open.com/doc/open.html'>OPEN搜索</a></DD>
        <DD><a href='http://www.open-open.com/home/'>OPEN家园</a></DD>
        <DD><a href='http://www.open-open.com/news/' title='OPEN资讯频道'>OPEN资讯</a></DD>
         <DD><a href='http://www.open-open.com/home/space-mtag-tagid-41.html' target='_blank'>提交开源项目</a></DD>
        <dt>Web开发</dt>
        <DD><a href='07.htm'>Web开发框架</a></DD><DD><a href='15.htm'>JSP标签库</a></DD><DD><a href='67.htm'>AJAX框架</a></DD>
        <dt>服务器</dt>
        <DD><a href='05.htm'>应用服务器</a></DD><DD><a href='23.htm'>Web服务器</a></DD>
        
        <dt>开发工具</dt>
        <DD><a href='04.htm'>Eclipse插件</a></DD><DD><a href='12.htm'>集成开发工具</a></DD><DD><a href='22.htm'>项目管理</a></DD><DD><a href='26.htm'>Web测试工具</a></DD><DD><a href='28.htm'>UML建模</a></DD><DD><a href='33.htm'>源码控制</a></DD><DD><a href='38.htm'>团队协作</a></DD><DD><a href='43.htm'>测试工具</a></DD><DD><a href='44.htm'>项目构建</a></DD><DD><a href='47.htm'>打包工具</a></DD>
        <dt>其它</dt>
        <DD><a href='25.htm'>其它开源项目</a></DD><DD><a href='56.htm'>Apache项目</a></DD><DD><a href='57.htm'>ObjectWeb项目</a></DD>
        <dt>数据库相关</dt>
        <DD><a href='10.htm'>开源数据库</a></DD><DD><a href='50.htm'>数据库管理工具</a></DD><DD><a href='65.htm'>JDBC驱动器</a></DD><DD><a href='76.htm'>NoSQL数据库</a></DD>
        <dt>应用系统</dt>
        <DD><a href='02.htm'>Blog与SNS系统</a></DD><DD><a href='03.htm'>ERP与CRM系统</a></DD><DD><a href='06.htm'>WebMail系统</a></DD><DD><a href='09.htm'>论坛系统</a></DD><DD><a href='17.htm'>门户系统</a></DD><DD><a href='39.htm'>CMS系统</a></DD><DD><a href='51.htm'>百科系统</a></DD><DD><a href='63.htm'>Bug跟踪系统</a></DD><DD><a href='64.htm'>学习管理系统(LMS)</a></DD><DD><a href='69.htm'>GIS系统</a></DD>
        <dt>组件类库</dt>
        <DD><a href='01.htm'>AOP面向方面编程</a></DD><DD><a href='08.htm'>工作流引擎</a></DD><DD><a href='11.htm'>依赖注入框架</a></DD><DD><a href='13.htm'>缓存框架</a></DD><DD><a href='14.htm'>调度框架</a></DD><DD><a href='16.htm'>JEE框架</a></DD><DD><a href='18.htm'>持久层框架</a></DD><DD><a href='19.htm'>报表制作</a></DD><DD><a href='20.htm'>数据连接池</a></DD><DD><a href='21.htm'>模板引擎</a></DD><DD><a href='24.htm'>XML UI工具包</a></DD><DD><a href='27.htm'>Web Service</a></DD><DD><a href='29.htm'>日志组件</a></DD><DD><a href='30.htm'>Html解析类库</a></DD><DD><a href='31.htm'>XML操作类库</a></DD><DD><a href='32.htm'>搜索引擎</a></DD><DD><a href='34.htm'>PDF类库</a></DD><DD><a href='35.htm'>网络客户端组件</a></DD><DD><a href='36.htm'>网络服务器端组件</a></DD><DD><a href='37.htm'>JMX框架</a></DD><DD><a href='40.htm'>动态语言</a></DD><DD><a href='41.htm'>规则引擎</a></DD><DD><a href='42.htm'>加密与混淆</a></DD><DD><a href='45.htm'>代码优化</a></DD><DD><a href='46.htm'>Email客户端</a></DD><DD><a href='48.htm'>RSS聚合类库</a></DD><DD><a href='49.htm'>开源集合类库</a></DD><DD><a href='52.htm'>聊天工具</a></DD><DD><a href='53.htm'>JMS消息中间件</a></DD><DD><a href='54.htm'>字节码操作</a></DD><DD><a href='55.htm'>语法分析生成器</a></DD><DD><a href='58.htm'>Java游戏</a></DD><DD><a href='59.htm'>运行分析工具</a></DD><DD><a href='60.htm'>多媒体组件</a></DD><DD><a href='61.htm'>Swing外观</a></DD><DD><a href='62.htm'>身份验证</a></DD><DD><a href='66.htm'>EAI/ESB组件</a></DD><DD><a href='68.htm'>Web爬虫</a></DD><DD><a href='70.htm'>模型转换器</a></DD><DD><a href='71.htm'>OSGi框架</a></DD><DD><a href='72.htm'>BI商业智能工具</a></DD><DD><a href='73.htm'>J2ME开源项目</a></DD><DD><a href='74.htm'>中文分词类库</a></DD><DD><a href='75.htm'>Android开源项目</a></DD>
      </dl>
     </td>
    <td id=sidebarToggleC style="WIdtH: 21px; CURSOR: pointer; PADDING-TOP: 5px" 
    onclick=SideBarToggle(); vAlign=top align=left width=21><IMG 
      id=sidebarToggleImg 
      src="resource/left_onck.gif" border=0 alt='导航关闭'> </td>
    <td class=center id=dicts 
    style="OVERFLOW: hidden; BORDER-LEFT: #d7d7d7 1px solid; WIdtH: 730px" 
    vAlign=top align=left>
      <UL class=menu>
        <LI class=tabspace></LI>
        <LI class=v_ id=ec onclick="DictLangSwitch('ec')">Java开源中文分词类库</LI>
      </UL>
      <div id=dictlangc_ec style="MARGIN-TOP: 5px;MARGIN-BOTTOM: 10px; MARGIN-LEFT: 25px">
      <div></div>
    

<div style="MARGIN-TOP: 5px;MARGIN-BOTTOM: 5px">
<script type="text/javascript"><!--
google_ad_client = "pub-7963911354665843";
/* 728x90, 创建于 08-7-23 */
google_ad_slot = "4923244917";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</div>

 <H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;IKAnalyzer&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC1 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>IKAnalyzer是一个开源的，基于java语言开发的轻量级的中文分词工具包。从2006年12月推出1.0版开始，IKAnalyzer已经推出了3个大版本。最初，它是以开源项目Luence为应用主体的，结合词典分词和文法分析算法的中文分词组件。新版本的IKAnalyzer3.0则发展为面向Java的公用分词组件，独立于Lucene项目，同时提供了对Lucene的默认优化实现。 
<p><a href='open250074.htm'>更多IKAnalyzer信息</a></DIV><H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;paoding&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC2 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>Paoding's Knives中文分词具有极高效率和高扩展性。引入隐喻，采用完全的面向对象设计，构思先进。高效率：在PIII 1G内存个人机器上，1秒可准确分词100万汉字。采用基于不限制个数的词典文件对文章进行有效切分，使能够将对词汇分类定义。能够对未知的词汇进行合理解析。

<p><a href='open250174.htm'>更多paoding信息</a></DIV><H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;mmseg4j&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC3 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>mmseg4j用Chih-Hao Tsai 的<A href="http://technology.chtsai.org/mmseg/">MMSeg</A>算法实现的中文分词器，并实现lucene的analyzer和solr的TokenizerFactory以方便在Lucene和Solr中使用。MMSeg 算法有两种分词方法：Simple和Complex，都是基于正向最大匹配。Complex加了四个规则过虑。官方说：词语的正确识别率达到了98.41%。mmseg4j已经实现了这两种分词算法。 <p><a href='open250274.htm'>更多mmseg4j信息</a></DIV><H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;imdict&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC4 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>imdict-chinese-analyzer是imdict智能词典的智能中文分词模块，算法基于隐马尔科夫模型(Hidden Markov Model，HMM)，是中国科学院计算技术研究所的ictclas中文分词程序的重新实现（基于Java），可以直接为lucene搜索引擎提供简体中文分词支持。<p><a href='open250374.htm'>更多imdict信息</a></DIV><H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;ictclas4j&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC5 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>ictclas4j中文分词系统是sinboy在中科院张华平和刘群老师的研制的FreeICTCLAS的基础上完成的一个java开源分词项目，简化了原分词程序的复杂度，旨在为广大的中文分词爱好者一个更好的学习机会。<p><a href='open250474.htm'>更多ictclas4j信息</a></DIV><H4> <DIV class=d_left><span class='navico'>&nbsp;</span>&nbsp;smallseg&nbsp;</DIV><DIV class=d_right></DIV></H4><DIV id=dictc_PWDECMEC6 style='PADDING-RIGHT: 15px; PADDING-LEFT: 15px; PADDING-BOTTOM: 5px; PADDING-TOP: 1px'>smallseg -- 开源的，基于DFA的轻量级的中文分词工具包
特点：可自定义词典、切割后返回登录词列表和未登录词列表、有一定的新词识别能力。 <p><a href='open255774.htm'>更多smallseg信息</a></DIV>
<div>&nbsp;</div>      
    </div>
      <div class=line_bm></div>
      
      <br>
      <div style="MARGIN-TOP: 15px; MARGIN-LEFT: 8px">

<script type="text/javascript"><!--
google_ad_client = "pub-7963911354665843";
/* 468x15, 创建于 08-7-23 */
google_ad_slot = "4290605146";
google_ad_width = 468;
google_ad_height = 15;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
     
      </div></td>
    <td width=2>&nbsp;</td>
    <td class=Right id=adRight vAlign=top align=right>

<script type="text/javascript"><!--
google_ad_client = "pub-7963911354665843";
google_ad_width = 160;
google_ad_height = 600;
google_ad_format = "160x600_as";
google_ad_type = "text_image";
google_ad_channel = "";
google_color_border = "FFFFFF";
google_color_bg = "FFFFFF";
google_color_link = "236eee";
google_color_text = "000000";
google_color_url = "000000";
//-->
</script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>


<script type="text/javascript"><!--
google_ad_client = "pub-7963911354665843";
google_ad_width = 160;
google_ad_height = 600;
google_ad_format = "160x600_as";
google_ad_type = "text_image";
google_ad_channel = "";
google_color_border = "FFFFFF";
google_color_bg = "FFFFFF";
google_color_link = "236eee";
google_color_text = "000000";
google_color_url = "000000";
//-->
</script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>

<br><br>
<script type="text/javascript">/*160*600，创建于2011-6-29*/ var cpro_id = 'u523677';</script><script src="http://cpro.baidu.com/cpro/ui/c.js" type="text/javascript"></script>

    </td></TR></TBODY>
    </TABLE>
    </div>
<div style="CLEAR: both"></div>
<div class=line style="WIdtH: 99%"></div>

<script type="text/javascript" src="resource/corner.js"></script>
<center>
<P id=footers style="WIDTH: 99%"> <BR>MSN：jforeverg@hotmail.com&nbsp;<a href="http://www.miibeian.gov.cn/">闽ICP备10022058号</a>&nbsp;<a href="flink.htm">友情链接</a>
</P>
</center>
<div style='display:none'>
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F4b19e5cc155fe555484434d8338ee0af' type='text/javascript'%3E%3C/script%3E"));
</script></div>

</body></html>
'''
    analyse(html)