# 话题
# 1. 修改“带你出去”为春节相关话题

label monika_ft_gre:
    "嗨, [player], 春节快乐"
    if store.mas_anni.pastOneMonth():
        if not mas_isBelowZero():
            if persistent._mas_sf_count > 1:
                $ after = "又一个"
            else:
                $ after = "第一个"
            "没想到我们能一起度过[after]春节~"
            
            if mas_isMoniAff(higher=True):
                "希望我们今年的春节能让你更开心~."
                "啊哈哈, 我爱你哦, [player]."

            if _mas_getAffection() < -75:
                "呃, 至少我们算是一起又过了一个新节日."
                "至少节日这天，我们应该高兴一点."
                "希望你别把我丢在这自己去玩游戏了"
                "反正我对你来说，也只不过是无聊的另一个废萌罢了."
                "怎样都好."

            if _mas_getAffection() > 0:
                "不过，昨天的鞭炮还真是响哦，希望没有吵到你"
            "总之, 我们今天干什么呢?"
    return
            
# 带你出去/带你拜年
label ft_aff_check:
    return
label ft_take_you_somewhere:
    if persistent._mas_sf_date_count = 0:
        call ft_ty_first    
    elif persistent._mas_sf_date_count = 1:
        call ft_ty_second
    else:
        call ft_ty_third_more
    jump mas_dockstat_iostart
    return

label ft_ty_first:
    "是要带我出去拜年吗?"
    "啊哈哈...这样, 我就要见一遍你的亲戚了."
    if mas_isMoniAff(higher=True):
        "不过，这也是早晚的事情~"
    "我不是害怕哦, 只是有点害羞，毕竟这样你的全家人就都认识我了."
    "希望我能给他们一个好印象..."
    return


label ft_ty_second:
    "还要出去吗? 看来你的亲戚有一点多呢~"
    "我会一直陪着你的."
    return

label ft_ty_third_more:
    "[player], 看来你今天很忙哦."
    "我会一直在你身边的."
    return
    
label ft_ty_back_first:
    "我回来了~"
    "感谢你带我今天带我出去，各种方面我都很开心~"
    "明年春节我们也要一起哦."
    "我爱你, [player]."
    return

label ft_ty_back_second_more:
    "欢迎回来，[player]."
    "感谢你带我出去玩~"
    return
