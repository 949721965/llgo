# 域名
DOMAIN = 'https://www.lagou.com'

# 起始地址池
START_URLS = {
    '技术': {
        '后端开发': {
            'Java': 'https://www.lagou.com/zhaopin/Java/%s',
            'C++': 'https://www.lagou.com/zhaopin/C%2B%2B/%s',
            'PHP': 'https://www.lagou.com/zhaopin/PHP/%s',
            '数据挖掘': 'https://www.lagou.com/zhaopin/shujuwajue/%s',
            '搜索算法': 'https://www.lagou.com/zhaopin/sousuosuanfa/%s',
            '精准推荐': 'https://www.lagou.com/zhaopin/jingzhuntuijian/%s',
            'C': 'https://www.lagou.com/zhaopin/C/%s',
            'C#': 'https://www.lagou.com/zhaopin/C%23/%s',
            '全栈工程师': 'https://www.lagou.com/zhaopin/quanzhangongchengshi/%s',
            '.NET': 'https://www.lagou.com/zhaopin/.NET/%s',
            'Hadoop': 'https://www.lagou.com/zhaopin/Hadoop/%s',
            'Python': 'https://www.lagou.com/zhaopin/Python/%s',
            'Delphi': 'https://www.lagou.com/zhaopin/Delphi/%s',
            'VB': 'https://www.lagou.com/zhaopin/VB/%s',
            'Perl': 'https://www.lagou.com/zhaopin/Perl/%s',
            'Ruby': 'https://www.lagou.com/zhaopin/Ruby/%s',
            'Node.js': 'https://www.lagou.com/zhaopin/Node.js/%s',
            'Go': 'https://www.lagou.com/zhaopin/go/%s',
            'ASP': 'https://www.lagou.com/zhaopin/asp/%s',
            'Shell': 'https://www.lagou.com/zhaopin/shell/%s',
            '区块链': 'https://www.lagou.com/zhaopin/qukuailian/%s',
            '后端开发其它': 'https://www.lagou.com/zhaopin/houduankaifaqita/%s'
        },
        '移动开发': {
            'HTML5': 'https://www.lagou.com/zhaopin/HTML5/%s',
            'Android': 'https://www.lagou.com/zhaopin/Android/%s',
            'iOS': 'https://www.lagou.com/zhaopin/iOS/%s',
            'WP': 'https://www.lagou.com/zhaopin/WP/%s',
            '移动开发其它': 'https://www.lagou.com/zhaopin/yidongkaifaqita/%s'
        },
        '前端开发': {
            'web前端': 'https://www.lagou.com/zhaopin/webqianduan/%s',
            'Flash': 'https://www.lagou.com/zhaopin/Flash/%s',
            'html5': 'https://www.lagou.com/zhaopin/html51/%s',
            'JavaScript': 'https://www.lagou.com/zhaopin/JavaScript/%s',
            'U3D': 'https://www.lagou.com/zhaopin/U3D/%s',
            'COCOS2D-X': 'https://www.lagou.com/zhaopin/COCOS2D-X/%s',
            '前端开发其它': 'https://www.lagou.com/zhaopin/qianduankaifaqita/%s'
        },
        '人工智能': {
            '深度学习': 'https://www.lagou.com/zhaopin/shenduxuexi/%s',
            '机器学习': 'https://www.lagou.com/zhaopin/jiqixuexi/%s',
            '图像处理': 'https://www.lagou.com/zhaopin/tuxiangchuli/%s',
            '图像识别': 'https://www.lagou.com/zhaopin/tuxiangshibie/%s',
            '语音识别': 'https://www.lagou.com/zhaopin/yuyinshibie/%s',
            '机器视觉': 'https://www.lagou.com/zhaopin/jiqishijue/%s',
            '算法工程师': 'https://www.lagou.com/zhaopin/suanfagongchengshi/%s',
            '自然语言处理': 'https://www.lagou.com/zhaopin/ziranyuyanchuli/%s'
        },
        '测试': {
            '测试工程师': 'https://www.lagou.com/zhaopin/ceshigongchengshi/%s',
            '自动化测试': 'https://www.lagou.com/zhaopin/zidonghuaceshi/%s',
            '功能测试': 'https://www.lagou.com/zhaopin/gongnengceshi/%s',
            '性能测试': 'https://www.lagou.com/zhaopin/xingnengceshi/%s',
            '测试开发': 'https://www.lagou.com/zhaopin/ceshikaifa/%s',
            '游戏测试': 'https://www.lagou.com/zhaopin/youxiceshi/%s',
            '白盒测试': 'https://www.lagou.com/zhaopin/baiheceshi/%s',
            '灰盒测试': 'https://www.lagou.com/zhaopin/huiheceshi/%s',
            '黑盒测试': 'https://www.lagou.com/zhaopin/heiheceshi/%s',
            '手机测试': 'https://www.lagou.com/zhaopin/shoujiceshi/%s',
            '硬件测试': 'https://www.lagou.com/zhaopin/yingjianceshi/%s',
            '测试经理': 'https://www.lagou.com/zhaopin/ceshijingli2/%s',
            '测试其它': 'https://www.lagou.com/zhaopin/ceshiqita/%s'
        },
        '运维': {
            '运维工程师': 'https://www.lagou.com/zhaopin/yunweigongchengshi/%s',
            '运维开发工程师': 'https://www.lagou.com/zhaopin/yunweikaifagongchengshi/%s',
            '网络工程师': 'https://www.lagou.com/zhaopin/wangluogongchengshi/%s',
            '系统工程师': 'https://www.lagou.com/zhaopin/xitonggongchengshi/%s',
            'IT支持': 'https://www.lagou.com/zhaopin/ITzhichi/%s',
            'IDC': 'https://www.lagou.com/zhaopin/idc/%s',
            'CDN': 'https://www.lagou.com/zhaopin/cdn/%s',
            'F5': 'https://www.lagou.com/zhaopin/f5/%s',
            '系统管理员': 'https://www.lagou.com/zhaopin/xitongguanliyuan/%s',
            '病毒分析': 'https://www.lagou.com/zhaopin/bingdufenxi/%s',
            'WEB安全': 'https://www.lagou.com/zhaopin/webanquan/%s',
            '网络安全': 'https://www.lagou.com/zhaopin/wangluoanquan/%s',
            '系统安全': 'https://www.lagou.com/zhaopin/xitonganquan/%s',
            '运维经理': 'https://www.lagou.com/zhaopin/yunweijingli/%s',
            '运维其它': 'https://www.lagou.com/zhaopin/yunweiqita/%s'
        },
        'DBA': {
            'MySQL': 'https://www.lagou.com/zhaopin/MySQL/%s',
            'SQLServer': 'https://www.lagou.com/zhaopin/SQLServer/%s',
            'Oracle': 'https://www.lagou.com/zhaopin/Oracle/%s',
            'DB2': 'https://www.lagou.com/zhaopin/DB2/%s',
            'MongoDB': 'https://www.lagou.com/zhaopin/MongoDB/%s',
            'ETL': 'https://www.lagou.com/zhaopin/etl/%s',
            'Hive': 'https://www.lagou.com/zhaopin/hive/%s',
            '数据仓库': 'https://www.lagou.com/zhaopin/shujucangku/%s',
            'DBA其它': 'https://www.lagou.com/zhaopin/dbaqita/%s'
        },
        '高端职位': {
            '技术经理': 'https://www.lagou.com/zhaopin/jishujingli/%s',
            '技术总监': 'https://www.lagou.com/zhaopin/jishuzongjian/%s',
            '架构师': 'https://www.lagou.com/zhaopin/jiagoushi/%s',
            'CTO': 'https://www.lagou.com/zhaopin/CTO/%s',
            '运维总监': 'https://www.lagou.com/zhaopin/yunweizongjian/%s',
            '技术合伙人': 'https://www.lagou.com/zhaopin/jishuhehuoren/%s',
            '项目总监': 'https://www.lagou.com/zhaopin/xiangmuzongjian/%s',
            '测试总监': 'https://www.lagou.com/zhaopin/ceshizongjian/%s',
            '安全专家': 'https://www.lagou.com/zhaopin/anquanzhuanjia/%s',
            '高端技术职位其它': 'https://www.lagou.com/zhaopin/gaoduanjishuzhiweiqita/%s'
        },
        '项目管理': {
            '项目经理': 'https://www.lagou.com/zhaopin/xiangmujingli/%s',
            '项目助理': 'https://www.lagou.com/zhaopin/xiangmuzhuli/%s'
        },
        '硬件开发': {
            '硬件': 'https://www.lagou.com/zhaopin/yingjian/%s',
            '嵌入式': 'https://www.lagou.com/zhaopin/qianrushi/%s',
            '自动化': 'https://www.lagou.com/zhaopin/zidonghua/%s',
            '单片机': 'https://www.lagou.com/zhaopin/danpianji/%s',
            '电路设计': 'https://www.lagou.com/zhaopin/dianlusheji/%s',
            '驱动开发': 'https://www.lagou.com/zhaopin/qudongkaifa/%s',
            '系统集成': 'https://www.lagou.com/zhaopin/xitongjicheng/%s',
            'FPGA开发': 'https://www.lagou.com/zhaopin/fpgakaifa/%s',
            'DSP开发': 'https://www.lagou.com/zhaopin/dspkaifa/%s',
            'ARM开发': 'https://www.lagou.com/zhaopin/armkaifa/%s',
            'PCB工艺': 'https://www.lagou.com/zhaopin/pcbgongyi/%s',
            '模具设计': 'https://www.lagou.com/zhaopin/mujusheji/%s',
            '热传导': 'https://www.lagou.com/zhaopin/rechuandao/%s',
            '材料工程师': 'https://www.lagou.com/zhaopin/cailiaogongchengshi/%s',
            '精益工程师': 'https://www.lagou.com/zhaopin/jingyigongchengshi/%s',
            '射频工程师': 'https://www.lagou.com/zhaopin/shepingongchengshi/%s',
            '硬件开发其它': 'https://www.lagou.com/zhaopin/yingjiankaifaqita/%s'
        },
        '企业软件': {
            '实施工程师': 'https://www.lagou.com/zhaopin/shishigongchengshi/%s',
            '售前工程师': 'https://www.lagou.com/zhaopin/shouqiangongchengshi/%s',
            '售后工程师': 'https://www.lagou.com/zhaopin/shouhougongchengshi/%s',
            'BI工程师': 'https://www.lagou.com/zhaopin/bigongchengshi/%s',
            '企业软件其它': 'https://www.lagou.com/zhaopin/qiyeruanjianqita/%s'
        }
    },
    '产品': {
        '产品经理': {
            '产品经理': 'https://www.lagou.com/zhaopin/chanpinjingli1/%s',
            '网页产品经理': 'https://www.lagou.com/zhaopin/wangyechanpinjingli/%s',
            '移动产品经理': 'https://www.lagou.com/zhaopin/yidongchanpinjingli/%s',
            '产品助理': 'https://www.lagou.com/zhaopin/chanpinzhuli/%s',
            '数据产品经理': 'https://www.lagou.com/zhaopin/shujuchanpinjingli/%s',
            '电商产品经理': 'https://www.lagou.com/zhaopin/dianshangchanpinjingli/%s',
            '游戏策划': 'https://www.lagou.com/zhaopin/youxicehua/%s',
            '产品实习生': 'https://www.lagou.com/zhaopin/chanpinshixisheng/%s'
        },
        '产品设计师': {
            '网页产品设计师': 'https://www.lagou.com/zhaopin/wangyechanpinshejishi/%s',
            '无线产品设计师': 'https://www.lagou.com/zhaopin/wuxianchanpinshejishi/%s'
        },
        '高端职位': {
            '产品部经理': 'https://www.lagou.com/zhaopin/chanpinbujingli/%s',
            '产品总监': 'https://www.lagou.com/zhaopin/chanpinzongjian/%s',
            '游戏制作人': 'https://www.lagou.com/zhaopin/youxizhizuoren/%s'
        }
    },
    '设计': {
        '视觉设计': {
            '视觉设计师': 'https://www.lagou.com/zhaopin/shijueshejishi/%s',
            '网页设计师': 'https://www.lagou.com/zhaopin/wangyeshejishi/%s',
            'Flash设计师': 'https://www.lagou.com/zhaopin/Flashshejishi/%s',
            'APP设计师': 'https://www.lagou.com/zhaopin/APPshejishi/%s',
            'UI设计师': 'https://www.lagou.com/zhaopin/UIshejishi/%s',
            '平面设计师': 'https://www.lagou.com/zhaopin/pingmianshejishi/%s',
            '美术设计师': 'https://www.lagou.com/zhaopin/meishushejishi%EF%BC%882D3D%EF%BC%89/%s',
            '广告设计师': 'https://www.lagou.com/zhaopin/guanggaoshejishi/%s',
            '多媒体设计师': 'https://www.lagou.com/zhaopin/duomeitishejishi/%s',
            '原画师': 'https://www.lagou.com/zhaopin/yuanhuashi/%s',
            '游戏特效': 'https://www.lagou.com/zhaopin/youxitexiao/%s',
            '游戏界面设计师': 'https://www.lagou.com/zhaopin/youxijiemianshejishi/%s',
            '游戏场景': 'https://www.lagou.com/zhaopin/youxichangjing/%s',
            '游戏角色': 'https://www.lagou.com/zhaopin/youxijiaose/%s',
            '游戏动作': 'https://www.lagou.com/zhaopin/youxidongzuo/%s'
        },
        '交互设计': {
            '交互设计师': 'https://www.lagou.com/zhaopin/jiaohushejishi1/%s',
            '无线交互设计师': 'https://www.lagou.com/zhaopin/wuxianjiaohushejishi/%s',
            '网页交互设计师': 'https://www.lagou.com/zhaopin/wangyejiaohushejishi/%s',
            '硬件交互设计师': 'https://www.lagou.com/zhaopin/yingjianjiaohushejishi/%s'
        },
        '用户研究':{
            '数据分析师': 'https://www.lagou.com/zhaopin/shujufenxishi/%s',
            '用户研究员': 'https://www.lagou.com/zhaopin/yonghuyanjiuyuan/%s',
            '游戏数值策划': 'https://www.lagou.com/zhaopin/youxishuzhicehua/%s'
        },
        '高端职位': {
            '设计经理': 'https://www.lagou.com/zhaopin/shejijinglizhuguan/%s',
            '设计总监': 'https://www.lagou.com/zhaopin/shejizongjian/%s',
            '视觉设计经理': 'https://www.lagou.com/zhaopin/shijueshejijinglizhuguan/%s',
            '视觉设计总监': 'https://www.lagou.com/zhaopin/shijueshejizongjian/%s',
            '交互设计经理': 'https://www.lagou.com/zhaopin/jiaohushejijinglizhuguan/%s',
            '交互设计总监': 'https://www.lagou.com/zhaopin/jiaohushejizongjian/%s',
            '用户研究经理': 'https://www.lagou.com/zhaopin/yonghuyanjiujinglizhuguan/%s'
        }
    },
    '运营': {
        '运营': {
            '用户运营': 'https://www.lagou.com/zhaopin/yonghuyunying/%s',
            '产品运营': 'https://www.lagou.com/zhaopin/chanpinyunying/%s',
            '数据运营': 'https://www.lagou.com/zhaopin/shujuyunying/%s',
            '内容运营': 'https://www.lagou.com/zhaopin/neirongyunying/%s',
            '活动运营': 'https://www.lagou.com/zhaopin/huodongyunying/%s',
            '商家运营': 'https://www.lagou.com/zhaopin/shangjiayunying/%s',
            '品类运营': 'https://www.lagou.com/zhaopin/pinleiyunying/%s',
            '游戏运营': 'https://www.lagou.com/zhaopin/youxiyunying/%s',
            '网络推广': 'https://www.lagou.com/zhaopin/wangluotuiguang/%s',
            '运营专员': 'https://www.lagou.com/zhaopin/yunyingzhuanyuan/%s',
            '网店运营': 'https://www.lagou.com/zhaopin/wangdianyunying/%s',
            '新媒体运营': 'https://www.lagou.com/zhaopin/xinmeitiyunying/%s',
            '海外运营': 'https://www.lagou.com/zhaopin/haiwaiyunying/%s',
            '运营经理': 'https://www.lagou.com/zhaopin/yunyingjingli/%s'
        },
        '编辑': {
            '副主编': 'https://www.lagou.com/zhaopin/fuzhubian/%s',
            '内容编辑': 'https://www.lagou.com/zhaopin/neirongbianji/%s',
            '文案策划': 'https://www.lagou.com/zhaopin/wenancehua/%s',
            '记者': 'https://www.lagou.com/zhaopin/jizhe/%s'
        },
        '客服': {
            '售前咨询': 'https://www.lagou.com/zhaopin/shouqianzixun/%s',
            '售后客服': 'https://www.lagou.com/zhaopin/shouhoukefu/%s',
            '淘宝客服': 'https://www.lagou.com/zhaopin/taobaokefu/%s',
            '客服经理': 'https://www.lagou.com/zhaopin/kefujingli/%s'
        },
        '高端职位': {
            '主编': 'https://www.lagou.com/zhaopin/zhubian/%s',
            '运营总监': 'https://www.lagou.com/zhaopin/yunyingzongjian/%s',
            'COO': 'https://www.lagou.com/zhaopin/COO/%s',
            '客服总监': 'https://www.lagou.com/zhaopin/kefuzongjian/%s'
        }
    },
    '市场': {
        '市场营销': {
            '市场营销': 'https://www.lagou.com/zhaopin/shichangshichangyingxiao1/%s',
            '市场策划': 'https://www.lagou.com/zhaopin/shichangcehua1/%s',
            '市场顾问': 'https://www.lagou.com/zhaopin/shichangguwen1/%s',
            '商务渠道': 'https://www.lagou.com/zhaopin/shangwuqudao2/%s',
            '商业数据分析': 'https://www.lagou.com/zhaopin/shangyeshjufenxi/%s',
            '活动策划': 'https://www.lagou.com/zhaopin/huodongcehua1/%s',
            '网络营销': 'https://www.lagou.com/zhaopin/wangluoyingxiao1/%s',
            '海外市场': 'https://www.lagou.com/zhaopin/haiwaishichang1/%s',
            '商务专员': 'https://www.lagou.com/zhaopin/shangwuzhuanyuan/%s'
        },
        '媒介公关': {
            '政府关系': 'https://www.lagou.com/zhaopin/zhengfuguanxi1/%s',
            '品牌公关': 'https://www.lagou.com/zhaopin/pinpaigongguan1/%s',
            '广告协调': 'https://www.lagou.com/zhaopin/guanggaoxietiao/%s',
            '媒介投放': 'https://www.lagou.com/zhaopin/meijietoufang/%s',
            '媒介合作': 'https://www.lagou.com/zhaopin/meijiehezuo/%s',
            '媒介顾问': 'https://www.lagou.com/zhaopin/meijieguwen/%s'
        },
        '品牌广告': {
            '广告创意': 'https://www.lagou.com/zhaopin/guanggaochuangyi/%s',
            '广告制作': 'https://www.lagou.com/zhaopin/guanggaozhizuo/%s',
            '广告文案': 'https://www.lagou.com/zhaopin/guanggaowenan/%s',
            '广告投放': 'https://www.lagou.com/zhaopin/guanggaotoufang/%s',
            '广告定价': 'https://www.lagou.com/zhaopin/guanggaodingwei/%s',
            '广告专员': 'https://www.lagou.com/zhaopin/guanggaozhuanyuan/%s',
            '品牌合作': 'https://www.lagou.com/zhaopin/pinpaihezuo/%s',
            '品牌策划': 'https://www.lagou.com/zhaopin/pinpaicehua/%s',
            '品牌专员': 'https://www.lagou.com/zhaopin/pinpaizhuanyuan/%s',
            '美术指导': 'https://www.lagou.com/zhaopin/meishuzhidao/%s'
        },
        '渠道推广': {
            '市场推广': 'https://www.lagou.com/zhaopin/shichangtuiguang1/%s',
            '渠道推广': 'https://www.lagou.com/zhaopin/qudaotuiguang1/%s',
            'SEO': 'https://www.lagou.com/zhaopin/SEO1/%s',
            'SEM': 'https://www.lagou.com/zhaopin/SEM1/%s'
        },
        '高端职位': {
            '策划经理': 'https://www.lagou.com/zhaopin/cehuajingli/%s',
            '媒介经理': 'https://www.lagou.com/zhaopin/meijiejingli1/%s',
            '市场总监': 'https://www.lagou.com/zhaopin/shichangzongjian1/%s',
            '公关总监': 'https://www.lagou.com/zhaopin/gongguanzoongjian/%s',
            '媒介总监': 'https://www.lagou.com/zhaopin/meijiezongjian/%s',
            '创意总监': 'https://www.lagou.com/zhaopin/chuangyizongjian/%s'
        }
    },
    '销售': {
        '销售': {
            '销售专员': 'https://www.lagou.com/zhaopin/xiaoshouzhuanyuan1/%s',
            '销售顾问': 'https://www.lagou.com/zhaopin/xiaoshouguwen1/%s',
            '销售经理': 'https://www.lagou.com/zhaopin/xiaoshoujingli1/%s',
            '客户代表': 'https://www.lagou.com/zhaopin/xiaoshoukehudaibiao/%s',
            '大客户代表': 'https://www.lagou.com/zhaopin/xiaoshoudakehudaibiao/%s',
            '客户经理': 'https://www.lagou.com/zhaopin/kehujingli/%s',
            '商务拓展': 'https://www.lagou.com/zhaopin/shangwutuozhan/%s',
            '渠道销售': 'https://www.lagou.com/zhaopin/xiaoshouqudaoxiaoshou/%s',
            '代理商销售': 'https://www.lagou.com/zhaopin/xiaoshoudailishangxiaoshou/%s',
            '电话销售': 'https://www.lagou.com/zhaopin/xiaoshoudianhuaxiaoshou/%s',
            '广告销售': 'https://www.lagou.com/zhaopin/guanggaoxiaoshou/%s',
            '信用卡销售': 'https://www.lagou.com/zhaopin/xinyongkaxiaoshou/%s',
            '保险销售': 'https://www.lagou.com/zhaopin/baoxianxiaoshou/%s',
            '销售工程师': 'https://www.lagou.com/zhaopin/xiaoshougongchengshi/%s',
            '商务渠道': 'https://www.lagou.com/zhaopin/xiaoshoushangwuqudao/%s',
            '其他销售': 'https://www.lagou.com/zhaopin/qitaxiaoshou/%s'
        },
        '销售管理': {
            '销售总监': 'https://www.lagou.com/zhaopin/xiaoshouzongjian1/%s',
            '商务总监': 'https://www.lagou.com/zhaopin/xiaoshoushangwuzongjian/%s',
            '区域总监': 'https://www.lagou.com/zhaopin/quyuzongjian/%s',
            '城市经理': 'https://www.lagou.com/zhaopin/chengshijingli/%s',
            '团队经理': 'https://www.lagou.com/zhaopin/tuanduijingli/%s',
            '销售VP': 'https://www.lagou.com/zhaopin/xiaoshouvp/%s',
            '商务主管': 'https://www.lagou.com/zhaopin/shangwuzhuguan/%s',
            '其他销售管理职位': 'https://www.lagou.com/zhaopin/qitaxiaoshouguanligangwei/%s'
        }
    },
    '职能': {
        '人力资源': {
            '人力资源': 'https://www.lagou.com/zhaopin/renliziyuan1/%s',
            '招聘': 'https://www.lagou.com/zhaopin/zhaopin/%s',
            'HRBP': 'https://www.lagou.com/zhaopin/HRBP/%s',
            '人事HR': 'https://www.lagou.com/zhaopin/renshiHR/%s',
            '培训经理': 'https://www.lagou.com/zhaopin/peixunjingli/%s',
            '薪资福利经理': 'https://www.lagou.com/zhaopin/xinzifulijingli/%s',
            '绩效考核经理': 'https://www.lagou.com/zhaopin/jixiaokaohejingli/%s',
            '员工关系': 'https://www.lagou.com/zhaopin/yuangongguanxi/%s'
        },
        '行政': {
            '助理': 'https://www.lagou.com/zhaopin/zhuli/%s',
            '前台': 'https://www.lagou.com/zhaopin/qiantai/%s',
            '行政': 'https://www.lagou.com/zhaopin/xingzheng1/%s',
            '总助': 'https://www.lagou.com/zhaopin/zongzhu/%s',
            '文秘': 'https://www.lagou.com/zhaopin/wenmi/%s'
        },
        '财务': {
            '会计': 'https://www.lagou.com/zhaopin/kuaiji/%s',
            '出纳': 'https://www.lagou.com/zhaopin/chuna/%s',
            '财务': 'https://www.lagou.com/zhaopin/caiwu1/%s',
            '结算': 'https://www.lagou.com/zhaopin/jiesuan/%s',
            '税务': 'https://www.lagou.com/zhaopin/shuiwu/%s',
            '审计': 'https://www.lagou.com/zhaopin/shenji/%s',
            '风控': 'https://www.lagou.com/zhaopin/fengkong/%s'
        },
        '法务': {
            '法务': 'https://www.lagou.com/zhaopin/fawu2/%s',
            '律师': 'https://www.lagou.com/zhaopin/lvshi/%s',
            '专利': 'https://www.lagou.com/zhaopin/zhuanli/%s'
        },
        '高端职位': {
            '行政总监': 'https://www.lagou.com/zhaopin/xingzhengzongjianjingli/%s',
            '财务总监': 'https://www.lagou.com/zhaopin/caiwuzongjianjingli/%s',
            'HRDHRM': 'https://www.lagou.com/zhaopin/HRDHRM/%s',
            'CFO': 'https://www.lagou.com/zhaopin/CFO/%s',
            'CEO': 'https://www.lagou.com/zhaopin/ceo/%s'
        }
    },
    '游戏': {
        '技术开发': {
            'H5游戏开发': 'https://www.lagou.com/zhaopin/H5youxikaifa/%s',
            '小游戏开发': 'https://www.lagou.com/zhaopin/xiaoyouxikaifa/%s',
            '游戏后端开发': 'https://www.lagou.com/zhaopin/youxihouduankaifa/%s',
            'C++游戏开发': 'https://www.lagou.com/zhaopin/C%2B%2Byouxikaifa/%s',
            'FLASH': 'https://www.lagou.com/zhaopin/youxiflash/%s',
            'COCOS2D-X': 'https://www.lagou.com/zhaopin/COCOS2D-X1/%s',
            'U3D': 'https://www.lagou.com/zhaopin/youxiU3D/%s',
            '游戏测试': 'https://www.lagou.com/zhaopin/youxiyouxiceshi/%s'
        },
        '产品策划': {
            '游戏制作人': 'https://www.lagou.com/zhaopin/youxizhipianren/%s',
            '游戏产品经理': 'https://www.lagou.com/zhaopin/youxichanpinjingli/%s',
            '游戏项目经理': 'https://www.lagou.com/zhaopin/youxixiangmujingli/%s',
            '游戏策划': 'https://www.lagou.com/zhaopin/youxiyouxicehua/%s',
            '剧情设计': 'https://www.lagou.com/zhaopin/juqingsheji/%s',
            '游戏文案': 'https://www.lagou.com/zhaopin/youxiwenan/%s'
        },
        '设计': {
            '游戏动画': 'https://www.lagou.com/zhaopin/youxidonghua/%s',
            '游戏原画': 'https://www.lagou.com/zhaopin/youxiyuanhua/%s',
            '游戏界面': 'https://www.lagou.com/zhaopin/youxijiemian/%s',
            '游戏场景': 'https://www.lagou.com/zhaopin/youxichangjing1/%s',
            '游戏角色': 'https://www.lagou.com/zhaopin/youxijuese/%s',
            '游戏动作': 'https://www.lagou.com/zhaopin/youxidongzuo1/%s',
            '游戏动效': 'https://www.lagou.com/zhaopin/youxidongxiao/%s',
            '游戏美工': 'https://www.lagou.com/zhaopin/youximeigong/%s'
        },
        '运营推广': {
            '游戏运营': 'https://www.lagou.com/zhaopin/youxiyunying1/%s',
            '游戏编辑': 'https://www.lagou.com/zhaopin/youxibianji/%s',
            '游戏推广': 'https://www.lagou.com/zhaopin/youxituiguang/%s',
            '手游推广': 'https://www.lagou.com/zhaopin/shouyoutuiguang/%s',
            '页游推广': 'https://www.lagou.com/zhaopin/yeyoutuiguang/%s'
        },
        '其他': {
            '游戏主播': 'https://www.lagou.com/zhaopin/youxizhuobo/%s',
            '游戏陪练': 'https://www.lagou.com/zhaopin/youxipeilian/%s',
            '游戏体验': 'https://www.lagou.com/zhaopin/youxitiyan/%s',
            '电竞主持': 'https://www.lagou.com/zhaopin/dianjingzhuchi/%s',
            '电竞讲师': 'https://www.lagou.com/zhaopin/dianjingjiangshi/%s'
        }
    }
}

# Xpath
XPATH_CONTENT = '/html[1]/body[1]/div[5]/div[2]/div[1]/div[3]/ul[1]'    
XPATH_HOMEPAGE = '/html[1]/body[1]/div[5]/div[2]/div[1]/div[3]/ul[1]/li/div[1]/div[1]/div[1]/a[1]/@href'
XPATH_JOBNAME = '/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/h2[1]/text()'
XPATH_SALARY = '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[1]/text()'
XPATH_LOCATION = '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[2]/text()'
XPATH_EXPERIENCE = '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[3]/text()'
XPATH_EDUCATION = '/html[1]/body[1]/div[5]/div[1]/div[1]/dd[1]/h3[1]/span[4]/text()'
XPATH_ADVANTAGE = '/html[1]/body[1]/div[7]/div[1]/dl[1]/dd[1]/p[1]/text()'
XPATH_DETAIL = '/html[1]/body[1]/div[7]/div[1]/dl[1]/dd[2]/div[1]/p/text()'
XPATH_COMPANYNAME = '/html[1]/body[1]/div[7]/div[2]/dl[1]/dt[1]/a[1]/div[1]/h3[1]/em[1]/text()'
XPATH_COMPANYFIELD = '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[1]/h4[1]/text()'
XPATH_FINANCING = '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[2]/h4[1]/text()'
XPATH_SCALE = '/html[1]/body[1]/div[7]/div[2]/dl[1]/dd[1]/ul[1]/li[3]/h4[1]/text()'

# 数据库操作语句


# cookie
COOKIE = [
    {'name':'login', 'value':'true'},
    {'name':'unick', 'value':'%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B76703'},
    {'name':'_putrc', 'value':'B8D0D8A14EC057D3123F89F2B170EADC'},
    {'name':'gate_login_token', 'value':'b116ffc0cefcf418c4756ef09dc85db0ac15e9dbc06f544d9cc3ccdd55cb78f4'},
    {'name':'LG_LOGIN_USER_ID', 'value':'1dfdee7b50f388035eaf8ed3f04ab3ed2f5ec7aac4907ef2b1d09d75bc936d9a'}
]
