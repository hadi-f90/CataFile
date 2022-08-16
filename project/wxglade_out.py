#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Mon Aug  1 19:18:37 2022
#
import os
import wx
from config import *

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

#  preferences file\


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN \
            | wx.CLOSE_BOX | wx.ICONIZE | wx.MINIMIZE_BOX | wx.RESIZE_BORDER \
            | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((596, 449))
        self.SetTitle("File Categorizer")

        self.main_panel = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(self.main_panel, wx.ID_ANY)
        self.notebook.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT,
                                      wx.FONTSTYLE_NORMAL,
                                      wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_1.Add(self.notebook, 1, wx.EXPAND, 0)

        self.action_pane = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.action_pane, "Actions")

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        source_folder_label = wx.StaticText(self.action_pane,
                                            wx.ID_ANY,
                                            "Source Folder:")
        source_folder_label.SetFont(wx.Font(12,
                                            wx.FONTFAMILY_DEFAULT,
                                            wx.FONTSTYLE_NORMAL,
                                            wx.FONTWEIGHT_NORMAL,
                                            0, ""))
        sizer_2.Add(source_folder_label, 1,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT | wx.TOP,
                    8)

        self.source_address_input = wx.TextCtrl(self.action_pane,
                                                wx.ID_ANY, "")
        self.source_address_input.SetBackgroundColour(wx.Colour(250, 255, 196))
        sizer_2.Add(self.source_address_input, 1, wx.ALL | wx.EXPAND, 8)

        destination_folder_label = wx.StaticText(self.action_pane, wx.ID_ANY,
                                                 "Destination Folder:",
                                                 style=wx.ALIGN_LEFT)
        destination_folder_label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT,
                                                 wx.FONTSTYLE_NORMAL,
                                                 wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_2.Add(destination_folder_label,
                    1,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT | wx.TOP,
                    8)

        self.destination_address_input = wx.TextCtrl(self.action_pane,
                                                     wx.ID_ANY, "")
        self.destination_address_input.SetBackgroundColour(
            wx.Colour(250, 255, 196))

        sizer_2.Add(self.destination_address_input, 1, wx.ALL | wx.EXPAND, 8)

        self.start_button = wx.Button(self.action_pane, wx.ID_APPLY, "&Start")
        self.start_button.SetFont(wx.Font(12,
                                          wx.FONTFAMILY_DEFAULT,
                                          wx.FONTSTYLE_NORMAL,
                                          wx.FONTWEIGHT_NORMAL, 0, ""))

        self.start_button.SetToolTip(
            "Start Detecting Files in Specified Addresses")
        self.start_button.SetFocus()
        sizer_2.Add(self.start_button, 2, wx.ALL | wx.EXPAND, 27)

        self.option_pane = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.option_pane, "Options")

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.file_processor_radio = wx.RadioBox(self.option_pane,
                                                wx.ID_ANY,
                                                "File processor:",
                                                choices=["Fleep", "Magic"],
                                                majorDimension=1,
                                                style=wx.RA_SPECIFY_ROWS)

        self.file_processor_radio.SetSelection(1)
        sizer_3.Add(self.file_processor_radio, 0, wx.ALL | wx.EXPAND, 4)

        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self.option_pane, wx.ID_ANY,
                                                 "Logging"),
                                    wx.HORIZONTAL)

        sizer_3.Add(sizer_4, 1, wx.EXPAND | wx.FIXED_MINSIZE | wx.SHAPED, 1)

        self.save_log_cb = wx.CheckBox(self.option_pane,
                                       wx.ID_ANY,
                                       "Save Log to File")

        sizer_4.Add(self.save_log_cb, 1, wx.ALL, 1)

        self.show_details_cb = wx.CheckBox(self.option_pane,
                                           wx.ID_ANY,
                                           "Show details to me")

        sizer_4.Add(self.show_details_cb, 1, wx.ALL, 1)

        sizer_7 = wx.StaticBoxSizer(wx.StaticBox(self.option_pane,
                                                 wx.ID_ANY,
                                                 "Log File Address"),
                                    wx.HORIZONTAL)

        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)

        self.log_file_address_input = wx.TextCtrl(self.option_pane,
                                                  wx.ID_ANY, "")
        self.log_file_address_input.Disabled = True

        self.log_file_address_input.Enable(False)
        sizer_7.Add(self.log_file_address_input, 1,
                    wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.calendar_cb_group = wx.RadioBox(self.option_pane,
                                             wx.ID_ANY,
                                             "Calendar  to be used in logs:",
                                             choices=["Khorsheedi (Persian)",
                                                      "Gergorian"],
                                             majorDimension=1,
                                             style=wx.RA_SPECIFY_ROWS)

        self.calendar_cb_group.SetSelection(0)
        sizer_3.Add(self.calendar_cb_group, 0,
                    wx.LEFT | wx.RIGHT | wx.SHAPED | wx.TOP, 3)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)

        sizer_8 = wx.StaticBoxSizer(wx.StaticBox(self.option_pane,
                                                 wx.ID_ANY, "Log level"),
                                    wx.VERTICAL)
        sizer_5.Add(sizer_8, 1, wx.LEFT | wx.RIGHT | wx.TOP, 1)

        self.log_level_combo = wx.ComboBox(self.option_pane,
                                           wx.ID_ANY,
                                           choices=["Debug", "Info",
                                                    "Warning", "Error",
                                                    "Critical"],
                                           style=wx.CB_DROPDOWN | wx.CB_SIMPLE)

        sizer_8.Add(self.log_level_combo, 1,
                    wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 4)

        self.AboutPane = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.AboutPane, "About")

        sizer_9 = wx.StaticBoxSizer(wx.StaticBox(self.AboutPane,
                                                 wx.ID_ANY, ""),
                                    wx.HORIZONTAL)

        About_label = wx.StaticText(self.AboutPane, wx.ID_ANY,
                                    "I created this tiny app for my own \
                                        personal use. \nIt may (not) \
                                            work on your system.\
                                                However, you may find it useful.")
        sizer_9.Add(About_label, 0, 0, 0)

        self.AboutPane.SetSizer(sizer_9)

        self.option_pane.SetSizer(sizer_3)

        self.action_pane.SetSizer(sizer_2)

        self.main_panel.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_TEXT,
                  self.change_source_address,
                  self.source_address_input)

        self.Bind(wx.EVT_TEXT,
                  self.change_destination_address,
                  self.destination_address_input)

        self.Bind(wx.EVT_BUTTON,
                  self.button_clicked,
                  self.start_button)

        self.Bind(wx.EVT_RADIOBOX,
                  self.change_file_processor,
                  self.file_processor_radio)

        self.Bind(wx.EVT_CHECKBOX,
                  self.change_save_to_log_status,
                  self.save_log_cb)

        self.Bind(wx.EVT_CHECKBOX,
                  self.change_show_details,
                  self.show_details_cb)

        self.Bind(wx.EVT_TEXT,
                  self.change_log_file_address,
                  self.log_file_address_input)

        self.Bind(wx.EVT_RADIOBOX,
                  self.change_calendar,
                  self.calendar_cb_group)

        self.Bind(wx.EVT_COMBOBOX,
                  self.change_log_level,
                  self.log_level_combo)
        # end wxGlade

    def change_source_address(self, event):
        pref.update_preferences({
            'source_dir': self.source_address_input.GetLineText(0)})

    def directory_selector(self, event):
        wx.DirSelector(message='Selected directory', default_path=wx.GetHomeDir(), style=0, parent=None)
        # A souble click runs this function

    def change_destination_address(self, event):
        pref.update_preferences({
            'destination_dir': self.destination_address_input.GetLineText(0)})

    def button_clicked(self, event):
        if '' == pref.get('source_dir'):
            wx.LogVerbose(f"No Source Directory specified!\n The result will be got from \n{wx.GetHomeDir()}")
            pref.update_preferences({'source_dir': wx.GetHomeDir()})

        elif '' == pref.get('destination_dir'):
            wx.LogVerbose(f"No Destination Directory specified!\n The result will be put in \n{os.getcwd()}")
            pref.update_preferences({'destination_dir': os.getcwd()})

        print('going through main process...')
        self.start_button.SetLabel('Stop')
        self.source_address_input.Disabled = True
        self.destination_address_input.Disabled = True
        self.start_button.SetBackgroundColour('#F8E71C')
        self.start_button.SetForegroundColour('#E81404')
        self.start_button.SetFont(wx.Font(14,
                                          wx.FONTFAMILY_DEFAULT,
                                          wx.FONTSTYLE_ITALIC,
                                          wx.FONTWEIGHT_BOLD,
                                          0, ""))
        self.Bind(wx.EVT_BUTTON,
                  self.stop_process,
                  self.start_button)

    def stop_process(self, event):  # wxGlade: MyFrame.<event_handler>
        self.start_button.SetLabel('Start')
        self.Bind(wx.EVT_BUTTON, self.button_clicked, self.start_button)
        self.start_button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.start_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        self.start_button.SetFont(wx.Font(14,
                                          wx.FONTFAMILY_DEFAULT,
                                          wx.FONTSTYLE_NORMAL,
                                          wx.FONTWEIGHT_NORMAL,
                                          0, ""))
        self.source_address_input.Disabled = False
        self.destination_address_input.Disabled = True
        print('Stopping...')
        # Add Stop Action function to stop

    def change_log_file_address(self, event):
        print("Event handler 'change_log_file_address' not implemented!")
        event.Skip()

    def change_file_processor(self, event):  # wxGlade: MyFrame.<event_handler>
        # pref.update_preferences({
        #     'file_processor': self.file_processor_radio.})
        print("Event handler 'change_file_processor' not implemented!")
        event.Skip()

    def change_save_to_log_status(self, event):
        if self.save_log_cb.IsChecked():
            self.log_file_address_input.Enable(True)
            pref.update_preferences({
                'save_log': True})
            print('Enabled')  # Todo: replace it with logging mechanism

        else:
            self.log_file_address_input.Enable(False)
            pref.update_preferences({
                'save_log': False})
            print('Disabled')  # Todo: replace it with logging mechanism

    def change_show_details(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'change_show_details' not implemented!")
        event.Skip()

    def change_log_file_address(self, event):
        pref.update_preferences({
            'destination_dir': self.log_file_address_input.GetLineText(0)})

    def change_calendar(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'change_calendar' not implemented!")
        event.Skip()

    def change_log_level(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'change_log_level' not implemented!")
        event.Skip()

# end of class MyFrame


class MainWindow(wx.App):
    def OnInit(self):
        self.main_frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True

# end of class MainWindow


if __name__ == "__main__":
    app = MainWindow(0)
    app.MainLoop()
