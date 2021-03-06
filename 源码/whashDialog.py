# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from pubsub import pub
import builtins
import json

###########################################################################
# Class whashDialog
###########################################################################


class whashDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"小波散列", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel281 = wx.Panel(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer341 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel291 = wx.Panel(self.m_panel281, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer351 = wx.BoxSizer(wx.HORIZONTAL)

        self.pan = wx.Panel(self.m_panel291, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer40 = wx.BoxSizer(wx.VERTICAL)

        gSizer12 = wx.GridSizer(5, 2, 10, 10)

        self.m_staticText18 = wx.StaticText(self.pan, wx.ID_ANY, u"哈希数值长度：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gSizer12.Add(self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        hash_sizeChoices = [u"8", u"16", u"32"]
        self.hash_size = wx.Choice(self.pan, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1), hash_sizeChoices, 0)
        self.hash_size.SetSelection(0)
        gSizer12.Add(self.hash_size, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText19 = wx.StaticText(self.pan, wx.ID_ANY, u"重设图像尺度：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        gSizer12.Add(self.m_staticText19, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        image_scaleChoices = [u"无", u"8", u"16"]
        self.image_scale = wx.Choice(self.pan, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1), image_scaleChoices, 0)
        self.image_scale.SetSelection(0)
        gSizer12.Add(self.image_scale, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText191 = wx.StaticText(self.pan, wx.ID_ANY, u"模式：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText191.Wrap(-1)
        gSizer12.Add(self.m_staticText191, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        modeChoices = [u"haar", u"db4"]
        self.mode = wx.Choice(self.pan, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1), modeChoices, 0)
        self.mode.SetSelection(0)
        gSizer12.Add(self.mode, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText1911 = wx.StaticText(self.pan, wx.ID_ANY, u"是否去掉低频段位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1911.Wrap(-1)
        gSizer12.Add(self.m_staticText1911, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        remove_max_haar_llChoices = [u"是", u"否"]
        self.remove_max_haar_ll = wx.Choice(self.pan, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1),
                                            remove_max_haar_llChoices, 0)
        self.remove_max_haar_ll.SetSelection(0)
        gSizer12.Add(self.remove_max_haar_ll, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText181 = wx.StaticText(self.pan, wx.ID_ANY, u"相似度阈值：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText181.Wrap(-1)
        gSizer12.Add(self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.THRESHOLD = wx.SpinCtrlDouble(self.pan, id=-1, size=wx.Size(80, -1), min=0.01, max=1, initial=0.7,
                                           inc=0.01)
        gSizer12.Add(self.THRESHOLD, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        bSizer40.Add(gSizer12, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.pan.SetSizer(bSizer40)
        self.pan.Layout()
        bSizer40.Fit(self.pan)
        bSizer351.Add(self.pan, 1, wx.ALIGN_CENTER, 5)

        self.m_panel291.SetSizer(bSizer351)
        self.m_panel291.Layout()
        bSizer351.Fit(self.m_panel291)
        bSizer341.Add(self.m_panel291, 1, wx.ALIGN_CENTER, 5)

        self.m_panel281.SetSizer(bSizer341)
        self.m_panel281.Layout()
        bSizer341.Fit(self.m_panel281)
        bSizer5.Add(self.m_panel281, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 10)

        gSizer2 = wx.GridSizer(1, 2, 0, 0)

        self.OkBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.OkBtn, 0, wx.ALIGN_LEFT, 5)

        self.CancelBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.CancelBtn, 0, wx.ALIGN_RIGHT, 5)

        bSizer5.Add(gSizer2, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        self.MainPanel.SetSizer(bSizer5)
        self.MainPanel.Layout()
        bSizer5.Fit(self.MainPanel)
        bSizer1.Add(self.MainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.Onclose)
        self.OkBtn.Bind(wx.EVT_BUTTON, self.OnOk)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.OnCancel)

        self.THRESHOLD.SetDigits(2)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Onclose(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def OnOk(self, event):
        whashData = {"hash_size": self.hash_size.GetSelection(), "image_scale": self.image_scale.GetSelection(),
                     "mode": self.mode.GetSelection(), "remove_max_haar_ll": self.remove_max_haar_ll.GetSelection(),
                     "THRESHOLD": self.THRESHOLD.GetValue()}
        with builtins.open("whashData.json", "w", encoding="UTF-8") as fp:
            json.dump(whashData, fp)
        pub.sendMessage("whashData", whashData=whashData)
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def OnCancel(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()
