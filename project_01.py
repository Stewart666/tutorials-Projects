import os
import time

print("welcome to install hyperLand OR Ubuntu 24.04")

installing_question = input("For installing Hyprland 'y' OR install Ubuntu 24.04 'n': ")

if installing_question == "y":  # call for installing Hyprland
    print('Your installing Hyprland')
    print('''
    files installing....................................................................................................
        ''')
    list_of_installings = [
        'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
        'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
        'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
        'https://deb.opera.com/opera-stable stable InRelease',
        'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
        'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
        'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
        'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
        'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
        'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
        'https://deb.opera.com/opera-stable stable InRelease',
        'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
        'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
        'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
        'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
        'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
        'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
        'https://deb.opera.com/opera-stable stable InRelease',
        'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
        'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
        'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving'
    ]
    for items in list_of_installings:
        time.sleep(2)
        print(items)
    time.sleep(3)
    print("installing completed")
    os.mkdir('hyprland')

elif installing_question == "n":  # call for installing Ubuntu 24.04
    print("Your install Ubuntu 24.04")
    if installing_question == "n":
        print('''
        files installing........................................................................................
            ''')
        list_of_Ubuntu_installings = [
            'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
            'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
            'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
            'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
            'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
            'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
            'https://deb.opera.com/opera-stable stable InRelease',
            'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
            'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
            'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
            'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
            'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
            'https://deb.opera.com/opera-stable stable InRelease',
            'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
            'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
            'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
            'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
            'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
            'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
            'https://deb.opera.com/opera-stable stable InRelease',
            'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
            'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
            'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving'
        ]
        for items in list_of_Ubuntu_installings:
            time.sleep(2)
            print(items)
        time.sleep(3)
        print("installing completed")

else:
    repeat = 3
    for number_of_repeat in range(repeat - 1):
        print("choose y(for installing hyprland) OR n(for installing Ubuntu 24.04)")
        installing_question = input('Do you want to install HyperLand?(y/n): ')
        if installing_question == "y":  # call for installing
            print('Your installing Hyprland')
            print('''
            files installing............................................................................................
                ''')
            list_of_installings = [
                'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
                'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                'https://deb.opera.com/opera-stable stable InRelease',
                'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
                'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
                'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                'https://deb.opera.com/opera-stable stable InRelease',
                'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
                'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
                'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                'https://deb.opera.com/opera-stable stable InRelease',
                'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving'
            ]
            for items in list_of_installings:
                time.sleep(2)
                print(items)
            time.sleep(3)
            print("installing completed")
            os.mkdir('hyprland')
            number_of_repeat = 0
        elif installing_question == "n":  # call for installing
            print("Your install Ubuntu 24.04")
            if installing_question == "n":  # call for installing
                print('''
                files installing........................................................................................
                    ''')
                list_of_Ubuntu_installings = [
                    'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                    'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                    'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
                    'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                    'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
                    'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                    'https://deb.opera.com/opera-stable stable InRelease',
                    'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                    'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                    'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
                    'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                    'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                    'https://deb.opera.com/opera-stable stable InRelease',
                    'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                    'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                    'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving',
                    'http://archive.ubuntu.com/ubuntu noble-backports InRelease',
                    'https://esm.ubuntu.com/apps/ubuntu noble-apps-updates InRelease',
                    'https://ppa.launchpadcontent.net/mark-pcnetspec/conky-manager-pm9/ubuntu noble InRelease',
                    'https://deb.opera.com/opera-stable stable InRelease',
                    'https://ppa.launchpadcontent.net/christian-boxdoerfer/fsearch-stable/ubuntu noble InRelease',
                    'https://dl.google.com/linux/chrome/deb stable InReleaseTemporary failure resolving dl.google.com',
                    'http://archive.ubuntu.com/ubuntu noble InReleaseTemporary failure resolving'
                ]
                for items in list_of_Ubuntu_installings:
                    time.sleep(2)
                    print(items)
                time.sleep(3)
                print("installing completed")
                os.mkdir('Ubuntu 24.04')
                number_of_repeat = 0

    print('END')
