from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_CMD', f'start{CMD_INDEX}')
        self.MirrorCommand = (f'mirror{CMD_INDEX}', f'm{CMD_INDEX}')
        self.UnzipMirrorCommand = (f'unzipmirror{CMD_INDEX}', f'uzm{CMD_INDEX}')
        self.ZipMirrorCommand = (f'zipmirror{CMD_INDEX}', f'zm{CMD_INDEX}')
        self.QbMirrorCommand = (f'qbmirror{CMD_INDEX}', f'qm{CMD_INDEX}')
        self.QbUnzipMirrorCommand = (f'qbunzipmirror{CMD_INDEX}', f'quzm{CMD_INDEX}')
        self.QbZipMirrorCommand = (f'qbzipmirror{CMD_INDEX}', f'qzm{CMD_INDEX}')
        self.YtdlCommand = (f'ytdl{CMD_INDEX}', f'y{CMD_INDEX}')
        self.YtdlZipCommand = (f'ytdlzip{CMD_INDEX}', f'yz{CMD_INDEX}')
        self.LeechCommand = (f'leech{CMD_INDEX}', f'l{CMD_INDEX}')
        self.UnzipLeechCommand = (f'unzipleech{CMD_INDEX}', f'uzl{CMD_INDEX}')
        self.ZipLeechCommand = (f'zipleech{CMD_INDEX}', f'zl{CMD_INDEX}')
        self.QbLeechCommand = (f'qbleech{CMD_INDEX}', f'ql{CMD_INDEX}')
        self.QbUnzipLeechCommand = (f'qbunzipleech{CMD_INDEX}', f'quzl{CMD_INDEX}')
        self.QbZipLeechCommand = (f'qbzipleech{CMD_INDEX}', f'qzl{CMD_INDEX}')
        self.YtdlLeechCommand = (f'ytdlleech{CMD_INDEX}', f'yl{CMD_INDEX}')
        self.YtdlZipLeechCommand = (f'ytdlzipleech{CMD_INDEX}', f'yzl{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_CMD', f'clone{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_CMD', f'count{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_CMD', f'del{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_CMD', f'cancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_CMD', f'cancelall{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_CMD', f'list{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_CMD', f'search{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_CMD', f'status{CMD_INDEX}')
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.SleepCommand = f'sleep{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.BtSelectCommand = f'btsel{CMD_INDEX}'
        self.RssListCommand = getCommand('RSSLIST_CMD', f'rsslist{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_CMD', f'rssget{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_CMD', f'rsssub{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_CMD', f'rssunsub{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_CMD', f'rssset{CMD_INDEX}')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_CMD', f'addleechlog{CMD_INDEX}')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_CMD', f'rmleechlog{CMD_INDEX}')
BotCommands = _BotCommands()
