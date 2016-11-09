#!/usr/bin/env python
import os.path
for module_name in [
'pysollib.acard',
'pysollib.actions',
'pysollib.app',
'pysollib.configobj.configobj',
'pysollib.configobj.validate',
'pysollib.customgame',
'pysollib.game',
'pysollib.gamedb',
'pysollib.games.acesup',
'pysollib.games.algerian',
'pysollib.games.auldlangsyne',
'pysollib.games.bakersdozen',
'pysollib.games.bakersgame',
'pysollib.games.beleagueredcastle',
'pysollib.games.bisley',
'pysollib.games.braid',
'pysollib.games.bristol',
'pysollib.games.buffalobill',
'pysollib.games.calculation',
'pysollib.games.camelot',
'pysollib.games.canfield',
'pysollib.games.capricieuse',
'pysollib.games.curdsandwhey',
'pysollib.games.dieboesesieben',
'pysollib.games.diplomat',
'pysollib.games.doublets',
'pysollib.games.eiffeltower',
'pysollib.games.fan',
'pysollib.games.fortythieves',
'pysollib.games.freecell',
'pysollib.games.glenwood',
'pysollib.games.golf',
'pysollib.games.grandduchess',
'pysollib.games.grandfathersclock',
'pysollib.games.gypsy',
'pysollib.games.harp',
'pysollib.games.headsandtails',
'pysollib.games.katzenschwanz',
'pysollib.games.klondike',
'pysollib.games.labyrinth',
'pysollib.games.larasgame',
'pysollib.games.mahjongg.mahjongg',
'pysollib.games.mahjongg.mahjongg1',
'pysollib.games.mahjongg.mahjongg2',
'pysollib.games.mahjongg.mahjongg3',
'pysollib.games.mahjongg.shisensho',
'pysollib.games.matriarchy',
'pysollib.games.montana',
'pysollib.games.montecarlo',
'pysollib.games.napoleon',
'pysollib.games.needle',
'pysollib.games.numerica',
'pysollib.games.osmosis',
'pysollib.games.parallels',
'pysollib.games.pasdedeux',
'pysollib.games.picturegallery',
'pysollib.games.pileon',
'pysollib.games.pushpin',
'pysollib.games.pyramid',
'pysollib.games.royalcotillion',
'pysollib.games.royaleast',
'pysollib.games.sanibel',
'pysollib.games.siebenbisas',
'pysollib.games.simplex',
'pysollib.games.special.hanoi',
'pysollib.games.special.memory',
'pysollib.games.special.pegged',
'pysollib.games.special.poker',
'pysollib.games.special.tarock',
'pysollib.games.spider',
'pysollib.games.sthelena',
'pysollib.games.sultan',
'pysollib.games.takeaway',
'pysollib.games.terrace',
'pysollib.games.threepeaks',
'pysollib.games.tournament',
'pysollib.games.ultra.dashavatara',
'pysollib.games.ultra.hanafuda',
'pysollib.games.ultra.hanafuda1',
'pysollib.games.ultra.hanafuda_common',
'pysollib.games.ultra.hexadeck',
'pysollib.games.ultra.larasgame',
'pysollib.games.ultra.matrix',
'pysollib.games.ultra.mughal',
'pysollib.games.ultra.tarock',
'pysollib.games.unionsquare',
'pysollib.games.wavemotion',
'pysollib.games.windmill',
'pysollib.games.yukon',
'pysollib.games.zodiac',
'pysollib.help',
'pysollib.hint',
'pysollib.images',
'pysollib.init',
'pysollib.layout',
'pysollib.macosx.appSupport',
'pysollib.main',
'pysollib.mfxutil',
'pysollib.move',
'pysollib.mygettext',
'pysollib.options',
'pysollib.pysolaudio',
'pysollib.pysolgtk.card',
'pysollib.pysolgtk.colorsdialog',
'pysollib.pysolgtk.edittextdialog',
'pysollib.pysolgtk.findcarddialog',
'pysollib.pysolgtk.fontsdialog',
'pysollib.pysolgtk.gameinfodialog',
'pysollib.pysolgtk.menubar',
'pysollib.pysolgtk.playeroptionsdialog',
'pysollib.pysolgtk.progressbar',
'pysollib.pysolgtk.pysoltree',
'pysollib.pysolgtk.selectcardset',
'pysollib.pysolgtk.selectgame',
'pysollib.pysolgtk.selecttile',
'pysollib.pysolgtk.soundoptionsdialog',
'pysollib.pysolgtk.statusbar',
'pysollib.pysolgtk.timeoutsdialog',
'pysollib.pysolgtk.tkcanvas',
'pysollib.pysolgtk.tkconst',
'pysollib.pysolgtk.tkhtml',
'pysollib.pysolgtk.tkstats',
'pysollib.pysolgtk.tkutil',
'pysollib.pysolgtk.tkwidget',
'pysollib.pysolgtk.tkwrap',
'pysollib.pysolgtk.toolbar',
'pysollib.pysolrandom',
'pysollib.pysoltk',
'pysollib.resource',
'pysollib.settings',
'pysollib.stack',
'pysollib.stats',
'pysollib.tile.colorsdialog',
'pysollib.tile.edittextdialog',
'pysollib.tile.findcarddialog',
'pysollib.tile.fontsdialog',
'pysollib.tile.gameinfodialog',
'pysollib.tile.menubar',
'pysollib.tile.playeroptionsdialog',
'pysollib.tile.progressbar',
'pysollib.tile.selectcardset',
'pysollib.tile.selectgame',
'pysollib.tile.selecttile',
'pysollib.tile.selecttree',
'pysollib.tile.solverdialog',
'pysollib.tile.soundoptionsdialog',
'pysollib.tile.statusbar',
'pysollib.tile.timeoutsdialog',
'pysollib.tile.tkhtml',
'pysollib.tile.tkstats',
'pysollib.tile.tktree',
'pysollib.tile.tkwidget',
'pysollib.tile.toolbar',
'pysollib.tile.ttk',
'pysollib.tile.wizarddialog',
'pysollib.tk.colorsdialog',
'pysollib.tk.edittextdialog',
'pysollib.tk.findcarddialog',
'pysollib.tk.fontsdialog',
'pysollib.tk.gameinfodialog',
'pysollib.tk.menubar',
'pysollib.tk.playeroptionsdialog',
'pysollib.tk.progressbar',
'pysollib.tk.selectcardset',
'pysollib.tk.selectgame',
'pysollib.tk.selecttile',
'pysollib.tk.selecttree',
'pysollib.tk.solverdialog',
'pysollib.tk.soundoptionsdialog',
'pysollib.tk.statusbar',
'pysollib.tk.tabpage',
'pysollib.tk.timeoutsdialog',
'pysollib.tk.tkhtml',
'pysollib.tk.tkstats',
'pysollib.tk.tktree',
'pysollib.tk.tkwidget',
'pysollib.tk.toolbar',
'pysollib.tk.wizarddialog',
'pysollib.ui.tktile.card',
'pysollib.ui.tktile.colorsdialog',
'pysollib.ui.tktile.menubar',
'pysollib.ui.tktile.solverdialog',
'pysollib.ui.tktile.tkcanvas',
'pysollib.ui.tktile.tkconst',
'pysollib.ui.tktile.tkutil',
'pysollib.ui.tktile.tkwrap',
'pysollib.util',
'pysollib.winsystems.aqua',
'pysollib.winsystems.common',
'pysollib.winsystems.win32',
'pysollib.winsystems.x11',
'pysollib.wizardpresets',
'pysollib.wizardutil',
]:
    open(os.path.join(".", "tests", "individually-importing", "import_" + module_name + ".py"), 'w').write('''#!/usr/bin/env python
import sys
sys.path.append("./tests/lib")
from TAP.Simple import plan, ok

plan(1)
sys.path.insert(0, ".")
import %(module_name)s
ok(1, "imported")
''' % { 'module_name': module_name })
