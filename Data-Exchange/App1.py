# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from PdfBuilder import PdfBuilder

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Report of Physical or Mental Examination", pos = wx.DefaultPosition, size = wx.Size( 919,890 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizerScrolled = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fistName = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fistName.Wrap( -1 )
		self.fistName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.fistName, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 15 )
		
		self.firstNameTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.firstNameTextCtrl, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lastname = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lastname.Wrap( -1 )
		self.lastname.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.lastname, 0, wx.ALIGN_CENTER|wx.ALL, 15 )
		
		self.lastNameTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.lastNameTxtCtrl, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.dataOfBirth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Date of Birth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataOfBirth.Wrap( -1 )
		self.dataOfBirth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.dataOfBirth, 0, wx.ALIGN_CENTER|wx.ALL, 15 )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.monthspinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 12, 1 )
		bSizer44.Add( self.monthspinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.datespinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 31, 1 )
		bSizer44.Add( self.datespinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearspinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1990", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1950, 2030, 1990 )
		bSizer44.Add( self.yearspinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer44, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.gender = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gender.Wrap( -1 )
		self.gender.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.gender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.genderChoiceBoxChoices = [ u"male", u"female" ]
		self.genderChoiceBox = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.genderChoiceBoxChoices, 0 )
		self.genderChoiceBox.SetSelection( 0 )
		bSizer2.Add( self.genderChoiceBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer2, 0, wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.street = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Street", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.street.Wrap( -1 )
		self.street.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.street, 0, wx.ALL, 15 )
		
		self.streetTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer3.Add( self.streetTextCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.city = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"City", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.city.Wrap( -1 )
		self.city.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.city, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.cityTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.cityTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.state = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"State", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.state.Wrap( -1 )
		self.state.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.state, 0, wx.ALL, 15 )
		
		self.stateTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.stateTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.zip = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Zip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zip.Wrap( -1 )
		self.zip.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.zip, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.zipTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.zipTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer3, 0, 0, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.caseid = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Case Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.caseid.Wrap( -1 )
		self.caseid.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.caseid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.caseIdtxtCrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.caseIdtxtCrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.category = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.category.Wrap( -1 )
		self.category.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.category, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.categoryTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.categoryTextCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer4, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tobecompletedbyphysician = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"TO BE COMPLETED BY EXAMINING PHYSICIAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tobecompletedbyphysician.Wrap( -1 )
		self.tobecompletedbyphysician.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.tobecompletedbyphysician, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizerScrolled.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.medicalhistory = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Medical History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.medicalhistory.Wrap( -1 )
		self.medicalhistory.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer7.Add( self.medicalhistory, 0, wx.ALL, 15 )
		
		self.medicalHistoryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer7.Add( self.medicalHistoryTxtCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.height = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.height.Wrap( -1 )
		self.height.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.height, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.heightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.heightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.weight = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weight.Wrap( -1 )
		self.weight.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.weight, 0, wx.ALL, 15 )
		
		self.weightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.weightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bloodpressure = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Blood Pressure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bloodpressure.Wrap( -1 )
		self.bloodpressure.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.bloodpressure, 0, wx.ALL, 15 )
		
		self.bloodPressureTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.bloodPressureTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.pulse  = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Pulse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pulse .Wrap( -1 )
		self.pulse .SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.pulse , 0, wx.ALL, 15 )
		
		self.pulseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.pulseTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.generalappearance = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"General Appearance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.generalappearance.Wrap( -1 )
		self.generalappearance.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.generalappearance, 0, wx.ALL, 15 )
		
		self.generalAppearanceTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.generalAppearanceTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.headscalp = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Head, Scalp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.headscalp.Wrap( -1 )
		self.headscalp.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.headscalp, 0, wx.ALL, 15 )
		
		self.headScalpTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.headScalpTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer8, 0, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ears = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Ears", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ears.Wrap( -1 )
		self.ears.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.ears, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.earsTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.earsTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.hearingleft = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Left", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingleft.Wrap( -1 )
		self.hearingleft.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingleft, 0, wx.ALL, 15 )
		
		self.hearingLeftTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingLeftTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.hearingright = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Right", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingright.Wrap( -1 )
		self.hearingright.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingright, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.hearingRightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingRightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nose = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Nose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nose.Wrap( -1 )
		self.nose.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.nose, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.noseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.noseTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.throat = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Throat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.throat.Wrap( -1 )
		self.throat.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.throat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.throatTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.throatTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.mouth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mouth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mouth.Wrap( -1 )
		self.mouth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.mouth, 0, wx.ALL, 15 )
		
		self.mouthTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.mouthTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer9, 0, 0, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.visualacuity = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Visual Acuity ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.visualacuity.Wrap( -1 )
		self.visualacuity.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.visualacuity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 35 )
		
		self.righteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"RIGHT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye1.Wrap( -1 )
		self.righteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.righteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		self.lefteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LEFT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye1.Wrap( -1 )
		self.lefteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.lefteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		
		bSizer10.Add( bSizer10_1, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer10_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.withoutglasses = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WITHOUT GLASSES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.withoutglasses.Wrap( -1 )
		self.withoutglasses.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2.Add( self.withoutglasses, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		bSizer10_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_2_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithoutglases.Wrap( -1 )
		self.distancewithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_1.Add( self.distancewithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.rightEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.leftEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_2_1.Add( bSizer10_2_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_2_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.nearwithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nearwithoutglases.Wrap( -1 )
		self.nearwithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_2.Add( self.nearwithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeNearWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_2.Add( self.rightEyeNearWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeNearWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_2.Add( self.leftEyeNearWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_2_1.Add( bSizer10_2_1_2, 1, wx.EXPAND, 5 )
		
		
		bSizer10_2.Add( bSizer10_2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer10_2, 1, wx.EXPAND, 5 )
		
		bSizer10_3 = wx.BoxSizer( wx.VERTICAL )
		
		self.withglasess = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WITH GLASSES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.withglasess.Wrap( -1 )
		self.withglasess.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3.Add( self.withglasess, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 15 )
		
		bSizer10_3_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_3_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithglases.Wrap( -1 )
		self.distancewithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_1.Add( self.distancewithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.rightEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.leftEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_3_1.Add( bSizer10_3_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_3_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.neardwithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neardwithglases.Wrap( -1 )
		self.neardwithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_2.Add( self.neardwithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeNearWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_2.Add( self.rightEyeNearWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeNearWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_2.Add( self.leftEyeNearWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_3_1.Add( bSizer10_3_1_2, 1, wx.EXPAND, 5 )
		
		
		bSizer10_3.Add( bSizer10_3_1, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer10_3, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer10, 0, 0, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fieldofvision = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Field of Vision", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fieldofvision.Wrap( -1 )
		self.fieldofvision.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_1.Add( self.fieldofvision, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer11.Add( bSizer11_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer11_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.limitationfieldofvision = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Is there any limitation in the field of vision?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.limitationfieldofvision.Wrap( -1 )
		self.limitationfieldofvision.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.limitationfieldofvision, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.righteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Right Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye.Wrap( -1 )
		self.righteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteye, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.righteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteyeCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lefteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Left Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye.Wrap( -1 )
		self.lefteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteye, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.lefteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteyeCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer11_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.neck = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neck.Wrap( -1 )
		self.neck.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_1.Add( self.neck, 0, wx.ALL, 15 )
		
		self.neckTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12_1.Add( self.neckTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer12_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer12_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chest = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Chest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chest.Wrap( -1 )
		self.chest.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_2.Add( self.chest, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.chestTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12_2.Add( self.chestTxtCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer12_2, 0, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer12, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cardiovascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiovascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiovascularsystem.Wrap( -1 )
		self.cardiovascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_1.Add( self.cardiovascularsystem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.cardiovascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13_1.Add( self.cardiovascularSystemTxtCtrl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer13.Add( bSizer13_1, 0, wx.EXPAND, 5 )
		
		bSizer13_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13_2_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.cardiacstatus = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiac Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiacstatus.Wrap( -1 )
		self.cardiacstatus.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1.Add( self.cardiacstatus, 0, wx.ALL, 15 )
		
		bSizer13_2_1_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.uncompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Uncompromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.uncompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.uncompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.slightlyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Slightly Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slightlyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.slightlyCompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Moderately Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.severelyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Severely Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.severelyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.severelyCompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer13_2_1.Add( bSizer13_2_1_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_1, 1, wx.EXPAND, 5 )
		
		bSizer13_2_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.prognosis1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Prognosis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis1.Wrap( -1 )
		self.prognosis1.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2.Add( self.prognosis1, 0, wx.ALL, 15 )
		
		bSizer13_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.goodPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.goodWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodWithTherapyPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.fairWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Fair With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fairWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.fairWithTherapyPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.guardedDespiteTherapyCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Guarded Despite Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.guardedDespiteTherapyCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.guardedDespiteTherapyCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer13_2_2.Add( bSizer13_2_2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_2, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer13_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_1_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Vascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vascularsystem.Wrap( -1 )
		self.vascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_1.Add( self.vascularsystem, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_1, 1, wx.EXPAND, 5 )
		
		bSizer14_1_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gastrointestinal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gastro Intestinal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gastrointestinal.Wrap( -1 )
		self.gastrointestinal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_2.Add( self.gastrointestinal, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_2, 1, wx.EXPAND, 5 )
		
		bSizer14_1_3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.genitourinary = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Genitourinary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.genitourinary.Wrap( -1 )
		self.genitourinary.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_3.Add( self.genitourinary, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_3, 1, wx.EXPAND, 5 )
		
		bSizer14_1_4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.hernia = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hernia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hernia.Wrap( -1 )
		self.hernia.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_4.Add( self.hernia, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_4, 1, wx.EXPAND, 5 )
		
		bSizer14_1_5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.musculoskeletal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Musculoskeletal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.musculoskeletal.Wrap( -1 )
		self.musculoskeletal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_5.Add( self.musculoskeletal, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_5, 1, wx.EXPAND, 5 )
		
		bSizer14_1_6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.neurological = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neurological", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neurological.Wrap( -1 )
		self.neurological.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_6.Add( self.neurological, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_6, 1, wx.EXPAND, 5 )
		
		bSizer14_1_7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.skin = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Skin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.skin.Wrap( -1 )
		self.skin.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_7.Add( self.skin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_7, 1, wx.EXPAND, 5 )
		
		bSizer14_1_8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.estimateofmentalcondition = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Estimate of Mental Condition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.estimateofmentalcondition.Wrap( -1 )
		self.estimateofmentalcondition.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_8.Add( self.estimateofmentalcondition, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_8, 1, wx.EXPAND, 5 )
		
		bSizer14_1_9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.diagnosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"DIAGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diagnosis.Wrap( -1 )
		self.diagnosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_9.Add( self.diagnosis, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_9, 1, wx.EXPAND, 5 )
		
		bSizer14_1_10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.prognosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"PROGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis.Wrap( -1 )
		self.prognosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_10.Add( self.prognosis, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_10, 1, wx.EXPAND, 5 )
		
		bSizer14_1_11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vacination = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Vacination", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vacination.Wrap( -1 )
		bSizer14_1_11.Add( self.vacination, 0, wx.ALL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_11, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer14_1, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		bSizer14_2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_1.Add( self.vascularSystemTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_1, 1, wx.EXPAND, 5 )
		
		bSizer14_2_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gastroIntestinalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_2.Add( self.gastroIntestinalTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_2, 1, wx.EXPAND, 5 )
		
		bSizer14_2_3 = wx.BoxSizer( wx.VERTICAL )
		
		self.genitourinaryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_3.Add( self.genitourinaryTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_3, 1, wx.EXPAND, 5 )
		
		bSizer14_2_4 = wx.BoxSizer( wx.VERTICAL )
		
		self.herniaTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_4.Add( self.herniaTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_4, 1, wx.EXPAND, 5 )
		
		bSizer14_2_5 = wx.BoxSizer( wx.VERTICAL )
		
		self.musculoskeletalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_5.Add( self.musculoskeletalTxtCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_5, 1, wx.EXPAND, 5 )
		
		bSizer14_2_6 = wx.BoxSizer( wx.VERTICAL )
		
		self.neurologicalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_6.Add( self.neurologicalTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_6, 1, wx.EXPAND, 5 )
		
		bSizer14_2_7 = wx.BoxSizer( wx.VERTICAL )
		
		self.skinTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_7.Add( self.skinTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_7, 1, wx.EXPAND, 5 )
		
		bSizer14_2_8 = wx.BoxSizer( wx.VERTICAL )
		
		self.estimateofMentalConditionTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_8.Add( self.estimateofMentalConditionTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_8, 1, wx.EXPAND, 5 )
		
		bSizer14_2_9 = wx.BoxSizer( wx.VERTICAL )
		
		self.diagnosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_9.Add( self.diagnosisTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_9, 1, wx.EXPAND, 5 )
		
		bSizer14_2_10 = wx.BoxSizer( wx.VERTICAL )
		
		self.prognosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_10.Add( self.prognosisTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_10, 1, wx.EXPAND, 5 )
		
		bSizer14_2_11 = wx.BoxSizer( wx.VERTICAL )
		
		self.vacinationTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14_2_11.Add( self.vacinationTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_11, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer14_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.submit = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Submit Form", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.submit.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer15.Add( self.submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizerScrolled )
		self.m_scrolledWindow1.Layout()
		bSizerScrolled.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.Submitted )
		self.dataList=[]
	
	def __del__( self ):
		pass
	
	
	def Submitted( self, event ):
		print self.monthspinCtrl.GetValue()
		print self.datespinCtrl.GetValue()
		print self.yearspinCtrl.GetValue()
		print self.genderChoiceBoxChoices[self.genderChoiceBox.GetSelection()]
		event.Skip()
		self.dataList.append([['<font size=12><b>First Name</b></font> ',self.firstNameTextCtrl.GetValue(),'<font size=12><b>Last Name</b></font> ',self.lastNameTxtCtrl.GetValue(),'<font size=12><b>Date of Birth</b></font> ',str(self.monthspinCtrl.GetValue())+" / "+str(self.datespinCtrl.GetValue())+" / "+str(self.yearspinCtrl.GetValue()),
			'<font size=12><b>Gender</b></font> ',self.genderChoiceBoxChoices[self.genderChoiceBox.GetSelection()]]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Street</b></font> ',self.streetTextCtrl.GetValue(),'<font size=12><b>City</b></font> ',self.cityTxtCtrl.GetValue(),
			'<font size=12><b>state</b></font> ',self.stateTxtCtrl.GetValue(),'<font size=12><b>Zipcode</b></font> ',self.zipTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Case Id</b></font> ',self.caseIdtxtCrl.GetValue(),'<font size=12><b>Category</b></font>',self.categoryTextCtrl.GetValue()]])
		self.dataList.append([['']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>TO BE COMPLETED BY EXAMINING PHYSICIAN</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Medical History</b></font> ',self.medicalHistoryTxtCtrl.GetValue()]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Height</b></font> ',self.heightTxtCtrl.GetValue(),'<font size=12><b>weight</b></font> ',self.weightTxtCtrl.GetValue(),
		'<font size=12><b>Blood Pressure</b></font> ',self.bloodPressureTxtCtrl.GetValue()]])
		self.dataList.append([['<font size=12><b>Pulse</b></font> ',self.pulseTxtCtrl.GetValue(),
		'<font size=12><b>General Appearance</b></font> ',self.generalAppearanceTxtCtrl.GetValue(),'<font size=12><b>Head,Scalp </b></font> ',self.headScalpTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Ears</b></font> ',self.earsTxtCtrl.GetValue(),'<font size=12><b>Hearing Left</b></font> ',self.hearingLeftTxtCtrl.GetValue(),
		'<font size=12><b>Hearing Right</b></font> ',self.hearingRightTxtCtrl.GetValue()]])
		self.dataList.append([['<font size=12><b>Nose</b></font> ',self.noseTxtCtrl.GetValue(),
		'<font size=12><b>Throat</b></font> ',self.throatTxtCtrl.GetValue(),'<font size=12><b>Mouth</b></font> ',self.mouthTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>WITHOUT GLASSES</b></font>','<font size=12><b>WITH GLASSES</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Visual Acuity </b></font>','<font size=12><b>Distance (20 ft.)</b></font>','<font size=12><b>Near (14 in.)</b></font>','<font size=12><b>Distance (20 ft.)</b></font>','<font size=12><b>Near (14 in.)</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>RIGHT EYE</b></font></font>',self.rightEyeDistanceWithOutGlassesTxtCtrl.GetValue(),self.rightEyeNearWithOutGlassesTxtCtrl.GetValue(),
			self.rightEyeDistanceWithGlassesTxtCtrl.GetValue(),self.rightEyeNearWithGlassesTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>LEFT EYE</b></font>',self.leftEyeDistanceWithOutGlassesTxtCtrl.GetValue(),self.leftEyeNearWithOutGlassesTxtCtrl.GetValue(),
			self.leftEyeDistanceWithGlassesTxtCtrl.GetValue(),self.leftEyeNearWithGlassesTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Field of Vision</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Is there any limitation in the field of vision?</b></font> ','<font size=12><b>Right Eye:</b></font> ',str(self.righteyeCheckBox.GetValue()),
		'<font size=12><b>Left Eye:</b></font> ',str(self.lefteyeCheckBox.GetValue())]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Neck</b></font> ',self.neckTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Chest</b></font> ',self.chestTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Cardio Vascular System</b></font> ',self.cardiovascularSystemTxtCtrl.GetValue()]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Cardiac Status</b></font> ','<font size=12><b>Prognosis</b></font>']])
		#self.dataList.append([['']])
		self.Status=[]
		if self.uncompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Uncompromised ')
		if self.slightlyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Slightly Compromised ')
		if self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.GetValue():
			self.Status.append('Moderately Compromised ')
		if self.severelyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Severely Compromised</b> ')
		else:
			self.Status.append(' ')

		if self.goodPrognsisCheckBox.GetValue():
			self.Status.append('Good ')
		if self.goodWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Good With Therapy ')
		if self.fairWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Fair With Therapy')
		if self.guardedDespiteTherapyCheckBox.GetValue():
			self.Status.append('Guarded Despite Therapy ')
		else:
			self.Status.append(' ')
       
		self.dataList.append([self.Status])
		#self.dataList.append([['']])


		self.dataList.append([['<font size=12><b>Vascular System</b></font> ',self.vascularSystemTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Gastro Intestinal</b></font> ',self.gastroIntestinalTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Genitourinary</b></font> ',self.genitourinaryTxtCtrl.GetValue()]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Hernia</b></font> ',self.herniaTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Musculo Skeletal</b></font> ',self.musculoskeletalTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Neurological</b></font> ',self.neurologicalTxtCtrl.GetValue()]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Skin</b></font> ',self.skinTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Estimate of Mental Condition</b></font> ',self.estimateofMentalConditionTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Diagnosis</b></font> ',self.diagnosisTxtCtrl.GetValue()]])
		#self.dataList.append([['']])

		self.dataList.append([['<font size=12><b>Prognosis</b></font> ',self.prognosisTxtCtrl.GetValue()]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Vacination</b></font> ',self.vacinationTxtCtrl.GetValue()]])
		#self.dataList.append([['']])


		self.pdfBuilder=PdfBuilder(self.lastNameTxtCtrl.GetValue())
		self.pdfBuilder.getDataList(self.dataList)
		print self.dataList
		event.Skip()


app=wx.App()
frame=Frame(None)
frame.Show()
frame.Maximize(True)
app.MainLoop()
