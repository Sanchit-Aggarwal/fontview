{
  'targets': [
    {
      'target_name': 'osx',
      'type': 'static_library',
      'conditions': [
        [
          'OS=="mac"', {
            'include_dirs': [
              'include_mac',
              'wxWidgets/include',
            ],
            'direct_dependent_settings': {
              'include_dirs': ['include_mac', 'wxWidgets/include'],
            },
            'dependencies': ['osx_carbon', 'osx_cocoa', 'unix'],
            'sources': [
              'wxWidgets/src/osx/accel.cpp',
              'wxWidgets/src/osx/anybutton_osx.cpp',
              'wxWidgets/src/osx/artmac.cpp',
              'wxWidgets/src/osx/bmpbuttn_osx.cpp',
              'wxWidgets/src/osx/brush.cpp',
              'wxWidgets/src/osx/button_osx.cpp',
              'wxWidgets/src/osx/checkbox_osx.cpp',
              'wxWidgets/src/osx/checklst_osx.cpp',
              'wxWidgets/src/osx/choice_osx.cpp',
              'wxWidgets/src/osx/combobox_osx.cpp',
              'wxWidgets/src/osx/dataview_osx.cpp',
              'wxWidgets/src/osx/datectrl_osx.cpp',
              'wxWidgets/src/osx/datetimectrl_osx.cpp',
              'wxWidgets/src/osx/dialog_osx.cpp',
              'wxWidgets/src/osx/dnd_osx.cpp',
              'wxWidgets/src/osx/fontutil.cpp',
              'wxWidgets/src/osx/fswatcher_fsevents.cpp',
              'wxWidgets/src/osx/gauge_osx.cpp',
              'wxWidgets/src/osx/glcanvas_osx.cpp',
              'wxWidgets/src/osx/imaglist.cpp',
              'wxWidgets/src/osx/listbox_osx.cpp',
              'wxWidgets/src/osx/menu_osx.cpp',
              'wxWidgets/src/osx/menuitem_osx.cpp',
              'wxWidgets/src/osx/minifram.cpp',
              'wxWidgets/src/osx/nonownedwnd_osx.cpp',
              'wxWidgets/src/osx/notebook_osx.cpp',
              'wxWidgets/src/osx/palette.cpp',
              'wxWidgets/src/osx/pen.cpp',
              'wxWidgets/src/osx/printdlg_osx.cpp',
              'wxWidgets/src/osx/radiobox_osx.cpp',
              'wxWidgets/src/osx/radiobut_osx.cpp',
              'wxWidgets/src/osx/scrolbar_osx.cpp',
              'wxWidgets/src/osx/slider_osx.cpp',
              'wxWidgets/src/osx/sound_osx.cpp',
              'wxWidgets/src/osx/spinbutt_osx.cpp',
              'wxWidgets/src/osx/srchctrl_osx.cpp',
              'wxWidgets/src/osx/statbox_osx.cpp',
              'wxWidgets/src/osx/statline_osx.cpp',
              'wxWidgets/src/osx/stattext_osx.cpp',
              'wxWidgets/src/osx/textctrl_osx.cpp',
              'wxWidgets/src/osx/textentry_osx.cpp',
              'wxWidgets/src/osx/tglbtn_osx.cpp',
              'wxWidgets/src/osx/timectrl_osx.cpp',
              'wxWidgets/src/osx/toolbar_osx.cpp',
              'wxWidgets/src/osx/toplevel_osx.cpp',
              'wxWidgets/src/osx/uiaction_osx.cpp',
              'wxWidgets/src/osx/utils_osx.cpp',
              'wxWidgets/src/osx/window_osx.cpp',
              'wxWidgets/src/osx/core/bitmap.cpp',
              'wxWidgets/src/osx/core/cfstring.cpp',
              'wxWidgets/src/osx/core/colour.cpp',
              'wxWidgets/src/osx/core/dcmemory.cpp',
              'wxWidgets/src/osx/core/display.cpp',
              'wxWidgets/src/osx/core/evtloop_cf.cpp',
              'wxWidgets/src/osx/core/fontenum.cpp',
              'wxWidgets/src/osx/core/hid.cpp',
              'wxWidgets/src/osx/core/hidjoystick.cpp',
              'wxWidgets/src/osx/core/mimetype.cpp',
              'wxWidgets/src/osx/core/printmac.cpp',
              'wxWidgets/src/osx/core/secretstore.cpp',
              'wxWidgets/src/osx/core/sockosx.cpp',
              'wxWidgets/src/osx/core/sound.cpp',
              'wxWidgets/src/osx/core/strconv_cf.cpp',
              'wxWidgets/src/osx/core/timer.cpp',
              'wxWidgets/src/osx/core/utilsexc_base.cpp',
              'wxWidgets/src/osx/core/utilsexc_cf.cpp',
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
              ],
            },
          },
        ],
      ],
    },
    {
      # wxWidgets needs its Carbon sources even for a pure Cocora build.
      'target_name': 'osx_carbon',
      'type': 'static_library',
      'conditions': [
        [
          'OS=="mac"', {
            'include_dirs': [
              'include_mac',
              'wxWidgets/include',
            ],
            'direct_dependent_settings': {
              'include_dirs': ['include_mac', 'wxWidgets/include'],
            },
            'sources': [
              'wxWidgets/src/osx/carbon/app.cpp',
              'wxWidgets/src/osx/carbon/clipbrd.cpp',
              'wxWidgets/src/osx/carbon/colordlg.cpp',
              'wxWidgets/src/osx/carbon/colordlgosx.mm',
              'wxWidgets/src/osx/carbon/control.cpp',
              'wxWidgets/src/osx/carbon/cursor.cpp',
              'wxWidgets/src/osx/carbon/dataobj.cpp',
              'wxWidgets/src/osx/carbon/dcclient.cpp',
              'wxWidgets/src/osx/carbon/dcprint.cpp',
              'wxWidgets/src/osx/carbon/dcscreen.cpp',
              'wxWidgets/src/osx/carbon/font.cpp',
              'wxWidgets/src/osx/carbon/fontdlg.cpp',
              'wxWidgets/src/osx/carbon/fontdlgosx.mm',
              'wxWidgets/src/osx/carbon/frame.cpp',
              'wxWidgets/src/osx/carbon/gdiobj.cpp',
              'wxWidgets/src/osx/carbon/graphics.cpp',
              'wxWidgets/src/osx/carbon/icon.cpp',
              'wxWidgets/src/osx/carbon/main.cpp',
              'wxWidgets/src/osx/carbon/mdi.cpp',
              'wxWidgets/src/osx/carbon/metafile.cpp',
              'wxWidgets/src/osx/carbon/overlay.cpp',
              'wxWidgets/src/osx/carbon/popupwin.cpp',
              'wxWidgets/src/osx/carbon/region.cpp',
              'wxWidgets/src/osx/carbon/renderer.cpp',
              'wxWidgets/src/osx/carbon/sound.cpp',
              'wxWidgets/src/osx/carbon/statbrma.cpp',
              #'wxWidgets/src/osx/carbon/thread.cpp',
              'wxWidgets/src/osx/carbon/utilscocoa.mm',
              #'wxWidgets/src/osx/carbon/wxmac.icns',
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/Carbon.framework',
              ],
            },
          },
        ],
      ],
    },
    {
      'target_name': 'osx_cocoa',
      'type': 'static_library',
      'conditions': [
        [
          'OS=="mac"', {
            'include_dirs': [
              'include_mac',
              'wxWidgets/include',
            ],
            'direct_dependent_settings': {
              'include_dirs': ['include_mac', 'wxWidgets/include'],
            },
            'sources': [
              'wxWidgets/src/osx/cocoa/aboutdlg.mm',
              'wxWidgets/src/osx/cocoa/activityindicator.mm',
              'wxWidgets/src/osx/cocoa/anybutton.mm',
              'wxWidgets/src/osx/cocoa/appprogress.mm',
              'wxWidgets/src/osx/cocoa/button.mm',
              'wxWidgets/src/osx/cocoa/checkbox.mm',
              'wxWidgets/src/osx/cocoa/choice.mm',
              'wxWidgets/src/osx/cocoa/colour.mm',
              'wxWidgets/src/osx/cocoa/combobox.mm',
              'wxWidgets/src/osx/cocoa/dataview.mm',
              'wxWidgets/src/osx/cocoa/datetimectrl.mm',
              'wxWidgets/src/osx/cocoa/dialog.mm',
              'wxWidgets/src/osx/cocoa/dirdlg.mm',
              'wxWidgets/src/osx/cocoa/dnd.mm',
              'wxWidgets/src/osx/cocoa/evtloop.mm',
              'wxWidgets/src/osx/cocoa/filedlg.mm',
              'wxWidgets/src/osx/cocoa/gauge.mm',
              'wxWidgets/src/osx/cocoa/glcanvas.mm',
              'wxWidgets/src/osx/cocoa/listbox.mm',
              'wxWidgets/src/osx/cocoa/mediactrl.mm',
              'wxWidgets/src/osx/cocoa/menu.mm',
              'wxWidgets/src/osx/cocoa/menuitem.mm',
              'wxWidgets/src/osx/cocoa/msgdlg.mm',
              'wxWidgets/src/osx/cocoa/nativewin.mm',
              'wxWidgets/src/osx/cocoa/nonownedwnd.mm',
              'wxWidgets/src/osx/cocoa/notebook.mm',
              'wxWidgets/src/osx/cocoa/notifmsg.mm',
              'wxWidgets/src/osx/cocoa/overlay.mm',
              'wxWidgets/src/osx/cocoa/power.mm',
              'wxWidgets/src/osx/cocoa/preferences.mm',
              'wxWidgets/src/osx/cocoa/printdlg.mm',
              'wxWidgets/src/osx/cocoa/radiobut.mm',
              'wxWidgets/src/osx/cocoa/scrolbar.mm',
              'wxWidgets/src/osx/cocoa/settings.mm',
              'wxWidgets/src/osx/cocoa/slider.mm',
              'wxWidgets/src/osx/cocoa/spinbutt.mm',
              'wxWidgets/src/osx/cocoa/srchctrl.mm',
              'wxWidgets/src/osx/cocoa/statbox.mm',
              'wxWidgets/src/osx/cocoa/statline.mm',
              'wxWidgets/src/osx/cocoa/stattext.mm',
              'wxWidgets/src/osx/cocoa/stdpaths.mm',
              'wxWidgets/src/osx/cocoa/taskbar.mm',
              'wxWidgets/src/osx/cocoa/textctrl.mm',
              'wxWidgets/src/osx/cocoa/tglbtn.mm',
              'wxWidgets/src/osx/cocoa/toolbar.mm',
              'wxWidgets/src/osx/cocoa/tooltip.mm',
              'wxWidgets/src/osx/cocoa/utils.mm',
              'wxWidgets/src/osx/cocoa/utils_base.mm',
              'wxWidgets/src/osx/cocoa/window.mm',
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
              ],
            },
          },
        ],
      ],
    },
    {
      'target_name': 'unix',
      'type': 'static_library',
      'conditions': [
        [
          'OS=="mac"', {
            'include_dirs': [
              'include_mac',
              'wxWidgets/include',
            ],
            'direct_dependent_settings': {
              'include_dirs': ['include_mac', 'wxWidgets/include'],
            },
            'sources': [
              'wxWidgets/src/unix/apptraits.cpp',
              'wxWidgets/src/unix/appunix.cpp',
              'wxWidgets/src/unix/dialup.cpp',
              'wxWidgets/src/unix/dir.cpp',
              #'wxWidgets/src/unix/displayx11.cpp',
              'wxWidgets/src/unix/dlunix.cpp',
              'wxWidgets/src/unix/epolldispatcher.cpp',
              'wxWidgets/src/unix/evtloopunix.cpp',
              'wxWidgets/src/unix/fdiounix.cpp',
              #'wxWidgets/src/unix/fontenum.cpp',
              #'wxWidgets/src/unix/fontutil.cpp',
              'wxWidgets/src/unix/fswatcher_inotify.cpp',
              'wxWidgets/src/unix/fswatcher_kqueue.cpp',
              #'wxWidgets/src/unix/glx11.cpp',
              #'wxWidgets/src/unix/joystick.cpp',
              #'wxWidgets/src/unix/mediactrl.cpp',
              #'wxWidgets/src/unix/mediactrl_gstplayer.cpp',
              'wxWidgets/src/unix/mimetype.cpp',
              'wxWidgets/src/unix/net.cpp',
              #'wxWidgets/src/unix/secretstore.cpp',
              'wxWidgets/src/unix/snglinst.cpp',
              'wxWidgets/src/unix/sockunix.cpp',
              #'wxWidgets/src/unix/sound.cpp',
              #'wxWidgets/src/unix/sound_sdl.cpp',
              #'wxWidgets/src/unix/stackwalk.cpp',
              #'wxWidgets/src/unix/stdpaths.cpp',
              #'wxWidgets/src/unix/taskbarx11.cpp',
              #'wxWidgets/src/unix/threadpsx.cpp',
              'wxWidgets/src/unix/timerunx.cpp',
              #'wxWidgets/src/unix/uiactionx11.cpp',
              'wxWidgets/src/unix/utilsunx.cpp',
              #'wxWidgets/src/unix/utilsx11.cpp',
              'wxWidgets/src/unix/wakeuppipe.cpp',
            ],
          },
        ],
      ],
    },
    {
      'target_name': 'core',
      'type': 'static_library',
      'sources': [
        'wxWidgets/src/common/accelcmn.cpp',
        'wxWidgets/src/common/accesscmn.cpp',
        'wxWidgets/src/common/addremovectrl.cpp',
        'wxWidgets/src/common/affinematrix2d.cpp',
        'wxWidgets/src/common/anidecod.cpp',
        'wxWidgets/src/common/animatecmn.cpp',
        'wxWidgets/src/common/any.cpp',
        'wxWidgets/src/common/appbase.cpp',
        'wxWidgets/src/common/appcmn.cpp',
        'wxWidgets/src/common/arcall.cpp',
        'wxWidgets/src/common/arcfind.cpp',
        'wxWidgets/src/common/archive.cpp',
        'wxWidgets/src/common/arrstr.cpp',
        'wxWidgets/src/common/artprov.cpp',
        'wxWidgets/src/common/artstd.cpp',
        'wxWidgets/src/common/arttango.cpp',
        'wxWidgets/src/common/base64.cpp',
        'wxWidgets/src/common/bmpbase.cpp',
        'wxWidgets/src/common/bmpbtncmn.cpp',
        'wxWidgets/src/common/bmpcboxcmn.cpp',
        'wxWidgets/src/common/bookctrl.cpp',
        'wxWidgets/src/common/btncmn.cpp',
        'wxWidgets/src/common/cairo.cpp',
        'wxWidgets/src/common/calctrlcmn.cpp',
        'wxWidgets/src/common/checkboxcmn.cpp',
        'wxWidgets/src/common/checklstcmn.cpp',
        'wxWidgets/src/common/choiccmn.cpp',
        'wxWidgets/src/common/clipcmn.cpp',
        'wxWidgets/src/common/clntdata.cpp',
        'wxWidgets/src/common/clrpickercmn.cpp',
        'wxWidgets/src/common/cmdline.cpp',
        'wxWidgets/src/common/cmdproc.cpp',
        'wxWidgets/src/common/cmndata.cpp',
        'wxWidgets/src/common/colourcmn.cpp',
        'wxWidgets/src/common/colourdata.cpp',
        'wxWidgets/src/common/combocmn.cpp',
        'wxWidgets/src/common/config.cpp',
        'wxWidgets/src/common/containr.cpp',
        'wxWidgets/src/common/convauto.cpp',
        'wxWidgets/src/common/cshelp.cpp',
        'wxWidgets/src/common/ctrlcmn.cpp',
        'wxWidgets/src/common/ctrlsub.cpp',
        'wxWidgets/src/common/datavcmn.cpp',
        'wxWidgets/src/common/datetime.cpp',
        'wxWidgets/src/common/datetimefmt.cpp',
        'wxWidgets/src/common/datstrm.cpp',
        'wxWidgets/src/common/dcbase.cpp',
        'wxWidgets/src/common/dcbufcmn.cpp',
        'wxWidgets/src/common/dcgraph.cpp',
        'wxWidgets/src/common/dcsvg.cpp',
        'wxWidgets/src/common/debugrpt.cpp',
        'wxWidgets/src/common/dircmn.cpp',
        'wxWidgets/src/common/dirctrlcmn.cpp',
        'wxWidgets/src/common/dlgcmn.cpp',
        'wxWidgets/src/common/dndcmn.cpp',
        'wxWidgets/src/common/dobjcmn.cpp',
        'wxWidgets/src/common/docmdi.cpp',
        'wxWidgets/src/common/docview.cpp',
        'wxWidgets/src/common/dpycmn.cpp',
        'wxWidgets/src/common/dseldlg.cpp',
        'wxWidgets/src/common/dummy.cpp',
        'wxWidgets/src/common/dynarray.cpp',
        'wxWidgets/src/common/dynlib.cpp',
        'wxWidgets/src/common/dynload.cpp',
        'wxWidgets/src/common/effects.cpp',
        'wxWidgets/src/common/encconv.cpp',
        'wxWidgets/src/common/event.cpp',
        'wxWidgets/src/common/evtloopcmn.cpp',
        'wxWidgets/src/common/extended.c',
        'wxWidgets/src/common/fddlgcmn.cpp',
        'wxWidgets/src/common/fdiodispatcher.cpp',
        'wxWidgets/src/common/ffile.cpp',
        'wxWidgets/src/common/file.cpp',
        'wxWidgets/src/common/fileback.cpp',
        'wxWidgets/src/common/fileconf.cpp',
        'wxWidgets/src/common/filectrlcmn.cpp',
        'wxWidgets/src/common/filefn.cpp',
        'wxWidgets/src/common/filehistorycmn.cpp',
        'wxWidgets/src/common/filename.cpp',
        'wxWidgets/src/common/filepickercmn.cpp',
        'wxWidgets/src/common/filesys.cpp',
        'wxWidgets/src/common/filtall.cpp',
        'wxWidgets/src/common/filtfind.cpp',
        'wxWidgets/src/common/fldlgcmn.cpp',
        'wxWidgets/src/common/fmapbase.cpp',
        'wxWidgets/src/common/fontcmn.cpp',
        'wxWidgets/src/common/fontdata.cpp',
        'wxWidgets/src/common/fontenumcmn.cpp',
        'wxWidgets/src/common/fontmap.cpp',
        # 'wxWidgets/src/common/fontmgrcmn.cpp',
        'wxWidgets/src/common/fontpickercmn.cpp',
        'wxWidgets/src/common/fontutilcmn.cpp',
        'wxWidgets/src/common/framecmn.cpp',
        'wxWidgets/src/common/fs_arc.cpp',
        'wxWidgets/src/common/fs_filter.cpp',
        'wxWidgets/src/common/fs_inet.cpp',
        'wxWidgets/src/common/fs_mem.cpp',
        'wxWidgets/src/common/fswatchercmn.cpp',
        'wxWidgets/src/common/ftp.cpp',
        'wxWidgets/src/common/gaugecmn.cpp',
        'wxWidgets/src/common/gbsizer.cpp',
        'wxWidgets/src/common/gdicmn.cpp',
        'wxWidgets/src/common/geometry.cpp',
        'wxWidgets/src/common/gifdecod.cpp',
        'wxWidgets/src/common/glcmn.cpp',
        'wxWidgets/src/common/graphcmn.cpp',
        'wxWidgets/src/common/gridcmn.cpp',
        'wxWidgets/src/common/hash.cpp',
        'wxWidgets/src/common/hashmap.cpp',
        'wxWidgets/src/common/headercolcmn.cpp',
        'wxWidgets/src/common/headerctrlcmn.cpp',
        'wxWidgets/src/common/helpbase.cpp',
        'wxWidgets/src/common/http.cpp',
        'wxWidgets/src/common/hyperlnkcmn.cpp',
        'wxWidgets/src/common/iconbndl.cpp',
        'wxWidgets/src/common/imagall.cpp',
        'wxWidgets/src/common/imagbmp.cpp',
        'wxWidgets/src/common/image.cpp',
        'wxWidgets/src/common/imagfill.cpp',
        # 'wxWidgets/src/common/imaggif.cpp',
        # 'wxWidgets/src/common/imagiff.cpp',
        # 'wxWidgets/src/common/imagjpeg.cpp',
        # 'wxWidgets/src/common/imagpcx.cpp',
        # 'wxWidgets/src/common/imagpng.cpp',
        # 'wxWidgets/src/common/imagpnm.cpp',
        # 'wxWidgets/src/common/imagtga.cpp',
        # 'wxWidgets/src/common/imagtiff.cpp',
        # 'wxWidgets/src/common/imagxpm.cpp',
        'wxWidgets/src/common/init.cpp',
        'wxWidgets/src/common/intl.cpp',
        'wxWidgets/src/common/ipcbase.cpp',
        'wxWidgets/src/common/languageinfo.cpp',
        'wxWidgets/src/common/layout.cpp',
        'wxWidgets/src/common/lboxcmn.cpp',
        'wxWidgets/src/common/list.cpp',
        'wxWidgets/src/common/listctrlcmn.cpp',
        'wxWidgets/src/common/log.cpp',
        'wxWidgets/src/common/longlong.cpp',
        'wxWidgets/src/common/markupparser.cpp',
        'wxWidgets/src/common/matrix.cpp',
        'wxWidgets/src/common/mediactrlcmn.cpp',
        'wxWidgets/src/common/memory.cpp',
        'wxWidgets/src/common/menucmn.cpp',
        'wxWidgets/src/common/mimecmn.cpp',
        'wxWidgets/src/common/modalhook.cpp',
        'wxWidgets/src/common/module.cpp',
        'wxWidgets/src/common/mousemanager.cpp',
        'wxWidgets/src/common/msgout.cpp',
        'wxWidgets/src/common/mstream.cpp',
        'wxWidgets/src/common/nbkbase.cpp',
        'wxWidgets/src/common/notifmsgcmn.cpp',
        'wxWidgets/src/common/numformatter.cpp',
        'wxWidgets/src/common/object.cpp',
        'wxWidgets/src/common/odcombocmn.cpp',
        'wxWidgets/src/common/overlaycmn.cpp',
        'wxWidgets/src/common/ownerdrwcmn.cpp',
        'wxWidgets/src/common/panelcmn.cpp',
        'wxWidgets/src/common/paper.cpp',
        'wxWidgets/src/common/persist.cpp',
        'wxWidgets/src/common/pickerbase.cpp',
        'wxWidgets/src/common/platinfo.cpp',
        'wxWidgets/src/common/popupcmn.cpp',
        'wxWidgets/src/common/powercmn.cpp',
        'wxWidgets/src/common/preferencescmn.cpp',
        'wxWidgets/src/common/prntbase.cpp',
        'wxWidgets/src/common/process.cpp',
        'wxWidgets/src/common/protocol.cpp',
        'wxWidgets/src/common/quantize.cpp',
        'wxWidgets/src/common/radiobtncmn.cpp',
        'wxWidgets/src/common/radiocmn.cpp',
        'wxWidgets/src/common/rearrangectrl.cpp',
        'wxWidgets/src/common/regex.cpp',
        'wxWidgets/src/common/rendcmn.cpp',
        'wxWidgets/src/common/rgncmn.cpp',
        'wxWidgets/src/common/richtooltipcmn.cpp',
        'wxWidgets/src/common/sckaddr.cpp',
        'wxWidgets/src/common/sckfile.cpp',
        'wxWidgets/src/common/sckipc.cpp',
        'wxWidgets/src/common/sckstrm.cpp',
        'wxWidgets/src/common/scrolbarcmn.cpp',
        'wxWidgets/src/common/secretstore.cpp',
        'wxWidgets/src/common/selectdispatcher.cpp',
        'wxWidgets/src/common/settcmn.cpp',
        'wxWidgets/src/common/sizer.cpp',
        'wxWidgets/src/common/slidercmn.cpp',
        'wxWidgets/src/common/socket.cpp',
        'wxWidgets/src/common/socketiohandler.cpp',
        'wxWidgets/src/common/spinbtncmn.cpp',
        'wxWidgets/src/common/spinctrlcmn.cpp',
        'wxWidgets/src/common/srchcmn.cpp',
        'wxWidgets/src/common/sstream.cpp',
        'wxWidgets/src/common/statbar.cpp',
        'wxWidgets/src/common/statbmpcmn.cpp',
        'wxWidgets/src/common/statboxcmn.cpp',
        'wxWidgets/src/common/statlinecmn.cpp',
        'wxWidgets/src/common/stattextcmn.cpp',
        'wxWidgets/src/common/stdpbase.cpp',
        'wxWidgets/src/common/stdstream.cpp',
        'wxWidgets/src/common/stockitem.cpp',
        'wxWidgets/src/common/stopwatch.cpp',
        'wxWidgets/src/common/strconv.cpp',
        'wxWidgets/src/common/stream.cpp',
        'wxWidgets/src/common/string.cpp',
        'wxWidgets/src/common/stringimpl.cpp',
        'wxWidgets/src/common/stringops.cpp',
        'wxWidgets/src/common/strvararg.cpp',
        'wxWidgets/src/common/sysopt.cpp',
        'wxWidgets/src/common/tarstrm.cpp',
        'wxWidgets/src/common/taskbarcmn.cpp',
        'wxWidgets/src/common/tbarbase.cpp',
        'wxWidgets/src/common/textbuf.cpp',
        'wxWidgets/src/common/textcmn.cpp',
        'wxWidgets/src/common/textentrycmn.cpp',
        'wxWidgets/src/common/textfile.cpp',
        'wxWidgets/src/common/textmeasurecmn.cpp',
        'wxWidgets/src/common/threadinfo.cpp',
        'wxWidgets/src/common/time.cpp',
        'wxWidgets/src/common/timercmn.cpp',
        'wxWidgets/src/common/timerimpl.cpp',
        'wxWidgets/src/common/tokenzr.cpp',
        'wxWidgets/src/common/toplvcmn.cpp',
        'wxWidgets/src/common/translation.cpp',
        'wxWidgets/src/common/treebase.cpp',
        'wxWidgets/src/common/txtstrm.cpp',
        'wxWidgets/src/common/uiactioncmn.cpp',
        'wxWidgets/src/common/unichar.cpp',
        'wxWidgets/src/common/uri.cpp',
        'wxWidgets/src/common/url.cpp',
        'wxWidgets/src/common/ustring.cpp',
        'wxWidgets/src/common/utilscmn.cpp',
        'wxWidgets/src/common/valgen.cpp',
        'wxWidgets/src/common/validate.cpp',
        'wxWidgets/src/common/valnum.cpp',
        'wxWidgets/src/common/valtext.cpp',
        'wxWidgets/src/common/variant.cpp',
        'wxWidgets/src/common/webview.cpp',
        'wxWidgets/src/common/webviewarchivehandler.cpp',
        'wxWidgets/src/common/webviewfshandler.cpp',
        'wxWidgets/src/common/wfstream.cpp',
        'wxWidgets/src/common/wincmn.cpp',
        'wxWidgets/src/common/windowid.cpp',
        'wxWidgets/src/common/wrapsizer.cpp',
        'wxWidgets/src/common/wxcrt.cpp',
        'wxWidgets/src/common/wxprintf.cpp',
        'wxWidgets/src/common/xlocale.cpp',
        'wxWidgets/src/common/xpmdecod.cpp',
        'wxWidgets/src/common/xti.cpp',
        'wxWidgets/src/common/xtistrm.cpp',
        'wxWidgets/src/common/xtixml.cpp',
        'wxWidgets/src/common/zipstrm.cpp',
        'wxWidgets/src/common/zstream.cpp',

        'wxWidgets/src/generic/aboutdlgg.cpp',
        #'wxWidgets/src/generic/accel.cpp',
        #'wxWidgets/src/generic/activityindicator.cpp',
        'wxWidgets/src/generic/animateg.cpp',
        'wxWidgets/src/generic/bannerwindow.cpp',
        #'wxWidgets/src/generic/bmpcboxg.cpp',
        'wxWidgets/src/generic/busyinfo.cpp',
        'wxWidgets/src/generic/buttonbar.cpp',
        'wxWidgets/src/generic/calctrlg.cpp',
        'wxWidgets/src/generic/caret.cpp',
        'wxWidgets/src/generic/choicbkg.cpp',
        'wxWidgets/src/generic/choicdgg.cpp',
        'wxWidgets/src/generic/clrpickerg.cpp',
        'wxWidgets/src/generic/collheaderctrlg.cpp',
        'wxWidgets/src/generic/collpaneg.cpp',
        #'wxWidgets/src/generic/colour.cpp',
        'wxWidgets/src/generic/colrdlgg.cpp',
        'wxWidgets/src/generic/combog.cpp',
        'wxWidgets/src/generic/commandlinkbuttong.cpp',
        'wxWidgets/src/generic/datavgen.cpp',
        'wxWidgets/src/generic/datectlg.cpp',
        'wxWidgets/src/generic/dbgrptg.cpp',
        'wxWidgets/src/generic/dcpsg.cpp',
        #'wxWidgets/src/generic/descrip.mms',
        'wxWidgets/src/generic/dirctrlg.cpp',
        'wxWidgets/src/generic/dirdlgg.cpp',
        'wxWidgets/src/generic/dragimgg.cpp',
        'wxWidgets/src/generic/editlbox.cpp',
        'wxWidgets/src/generic/fdrepdlg.cpp',
        'wxWidgets/src/generic/filectrlg.cpp',
        'wxWidgets/src/generic/filedlgg.cpp',
        'wxWidgets/src/generic/filepickerg.cpp',
        'wxWidgets/src/generic/fontdlgg.cpp',
        'wxWidgets/src/generic/fontpickerg.cpp',
        'wxWidgets/src/generic/fswatcherg.cpp',
        'wxWidgets/src/generic/graphicc.cpp',
        'wxWidgets/src/generic/grid.cpp',
        'wxWidgets/src/generic/gridctrl.cpp',
        'wxWidgets/src/generic/grideditors.cpp',
        'wxWidgets/src/generic/gridsel.cpp',
        'wxWidgets/src/generic/headerctrlg.cpp',
        'wxWidgets/src/generic/helpext.cpp',
        'wxWidgets/src/generic/htmllbox.cpp',
        'wxWidgets/src/generic/hyperlinkg.cpp',
        #'wxWidgets/src/generic/icon.cpp',
        #'wxWidgets/src/generic/imaglist.cpp',
        'wxWidgets/src/generic/infobar.cpp',
        'wxWidgets/src/generic/laywin.cpp',
        #'wxWidgets/src/generic/listbkg.cpp',
        'wxWidgets/src/generic/listctrl.cpp',
        'wxWidgets/src/generic/logg.cpp',
        'wxWidgets/src/generic/markuptext.cpp',
        'wxWidgets/src/generic/mask.cpp',
        #'wxWidgets/src/generic/mdig.cpp',
        'wxWidgets/src/generic/msgdlgg.cpp',
        #'wxWidgets/src/generic/notebook.cpp',
        'wxWidgets/src/generic/notifmsgg.cpp',
        'wxWidgets/src/generic/numdlgg.cpp',
        'wxWidgets/src/generic/odcombo.cpp',
        'wxWidgets/src/generic/paletteg.cpp',
        'wxWidgets/src/generic/preferencesg.cpp',
        'wxWidgets/src/generic/printps.cpp',
        'wxWidgets/src/generic/prntdlgg.cpp',
        'wxWidgets/src/generic/progdlgg.cpp',
        'wxWidgets/src/generic/propdlg.cpp',
        #'wxWidgets/src/generic/regiong.cpp',
        'wxWidgets/src/generic/renderg.cpp',
        'wxWidgets/src/generic/richmsgdlgg.cpp',
        'wxWidgets/src/generic/richtooltipg.cpp',
        'wxWidgets/src/generic/sashwin.cpp',
        'wxWidgets/src/generic/scrlwing.cpp',
        'wxWidgets/src/generic/selstore.cpp',
        'wxWidgets/src/generic/spinctlg.cpp',
        'wxWidgets/src/generic/splash.cpp',
        'wxWidgets/src/generic/splitter.cpp',
        'wxWidgets/src/generic/srchctlg.cpp',
        'wxWidgets/src/generic/statbmpg.cpp',
        #'wxWidgets/src/generic/statline.cpp',
        'wxWidgets/src/generic/stattextg.cpp',
        'wxWidgets/src/generic/statusbr.cpp',
        'wxWidgets/src/generic/tabg.cpp',
        'wxWidgets/src/generic/textdlgg.cpp',
        'wxWidgets/src/generic/textmeasure.cpp',
        'wxWidgets/src/generic/timectrlg.cpp',
        'wxWidgets/src/generic/timer.cpp',
        'wxWidgets/src/generic/tipdlg.cpp',
        'wxWidgets/src/generic/tipwin.cpp',
        'wxWidgets/src/generic/toolbkg.cpp',
        'wxWidgets/src/generic/treebkg.cpp',
        'wxWidgets/src/generic/treectlg.cpp',
        'wxWidgets/src/generic/treelist.cpp',
        'wxWidgets/src/generic/vlbox.cpp',
        'wxWidgets/src/generic/vscroll.cpp',
        'wxWidgets/src/generic/wizard.cpp',
      ],
      'include_dirs': [
        'wxWidgets/include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'wxWidgets/include',
        ],
      },
      'conditions': [
        [
          'OS=="mac"', {
            'include_dirs': ['include_mac'],
            'dependencies': ['osx'],
            'direct_dependent_settings': {
              'include_dirs': ['include_mac'],
            },
            'sources': [
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
                '$(SDKROOT)/System/Library/Frameworks/Carbon.framework',
                '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
                '$(SDKROOT)/System/Library/Frameworks/IOKit.framework',
              ],
            },
          },
        ],
      ],
    },
  ],

  'target_defaults': {
    'xcode_settings': {
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++14',
      'CLANG_CXX_LIBRARY': 'libc++',
    },
  },
}
