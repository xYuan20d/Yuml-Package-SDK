from ._apis import Globals, Default, Log


class YAPIEngine:
    def __init__(self, raw):
        self.hook: Default.hook = raw.set_hook
        self.string: Default.string = raw.string
        self.onClicked: Default.onClicked = raw.clicked
        self.callBlack: Default.call_block = raw.call_block

        self.globals: Globals = raw.API_G
        self.LOG: Log = raw
