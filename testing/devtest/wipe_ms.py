# quickly clear all multisig wallets installed
from main import settings
from ux import restore_menu

if settings.get('multisig'):
    del settings.current['multisig']
    settings.save()

    print("cleared multisigs")

restore_menu()
