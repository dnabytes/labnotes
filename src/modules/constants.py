DEFAULT_N_LINES = {
    'readall': 7,
    'read': 10
}

HELP = (
    'Usage: labnotes OPTION',
    '',
    'Options:',
    '',
    '  read [n_notes:int or "all"] (default 10)',
    '  readall [n_notes:int or "all"] (default 7)',
    '  add',
    '  search query:str'
)

OPTIONS_NEED_CONTENT = [
    'read',
    'readall',
    'search'
]

OPTIONS_ALL = [
    'help',
    'add',
    'read',
    'readall',
    'search'
]
