
init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="春节",
        description="为MAS添加春节节日",
        version='1.0.0',
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="春节",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="MAS-Spring-Festival-Submod",
            update_dir="",
            attachment_id=None
        )

init -989 python:
    if not store.mas_submod_utils.isSubmodInstalled("话题整合包"):
        raise Exception("'春节'子模组需要'话题整合包'作为前置\n'Spring Festival submod' REQUIRE 'Dialogue-Packs submod'")