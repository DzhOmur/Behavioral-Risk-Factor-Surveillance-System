import numpy as np
import pandas as pd

colspecs = [
    (0, 2),   # _STATE (State FIPS Code)
	(16, 18), # FMONTH (File Month)
	(18, 26), # IDATE (Interview Date)
	(18, 20), # IMONTH (Interview Month)
	(20, 22), # IDAY (Interview Day)
	(22, 26), # IYEAR (Interview Year)
	(31, 35), # DISPCODE (Final Disposition)
	(35, 45), # SEQNO (Annual Sequence Number)
	(35, 45), # _PSU (Primary Sampling Unit (Equal to Annual Sequence Number))
	(62, 63), # CTELENM1 (Is this     (phone number)     ?)
	(63, 64), # PVTRESD1 (Is this a private residence?   [READ ONLY IF NECESSARY: “By private residence, we mean someplace like a house or apartment.”])
	(64, 65), # COLGHOUS (Do you live in college housing?)
	(65, 66), # STATERE1 (Do you currently live in  ____(state)____?)
	(66, 67), # CELPHON1 (Is this a cell telephone?)
	(67, 68), # LADULT1 (Are you 18 years of age or older?)
	(68, 70), # NUMADULT (I need to randomly select one adult who lives in your household to be interviewed. Excluding adults living away from home, such as students away at college, how many members of your household, including yourself, are 18 years of age or older?)
	(70, 71), # RESPSLC1 (The person in your household that I need to speak with is the adult with the most recent birthday. Are you the adult with the most recent birthday?)
	(71, 72), # LANDSEX2 (Are you?)
	(72, 73), # LNDSXBRT (What was your sex at birth? Was it male or female?)
	(73, 74), # SAFETIME (Is this a safe time to talk with you?)
	(74, 75), # CTELNUM1 (Is this     (phone number)     ?)
	(75, 76), # CELLFON5 (Is this a cell phone?)
	(76, 77), # CADULT1 (Are you 18 years of age or older?)
	(77, 78), # CELLSEX2 (Are you?)
	(78, 79), # CELSXBRT (What was your sex at birth? Was it male or female?)
	(79, 80), # PVTRESD3 (Do you live in a private residence?  (By private residence, we mean someplace like a house or apartment.))
	(80, 81), # CCLGHOUS (Do you live in college housing?)
	(81, 82), # CSTATE1 (Do you currently live in  ____(state)____?)
	(84, 85), # LANDLINE (Do you also have a landline telephone in your home that is used to make and receive calls?)
	(85, 87), # HHADULT (How many members of your household, including yourself, are 18 years of age or older?)
	(87, 88), # SEXVAR (Sex of Respondent)
	(100, 101), # GENHLTH (Would you say that in general your health is:)
	(101, 103), # PHYSHLTH (Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?)
	(103, 105), # MENTHLTH (Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?)
	(105, 107), # POORHLTH (During the past 30 days, for about how many days did poor physical or mental health keep you from doing your usual activities, such as self-care, work, or recreation?)
	(107, 109), # PRIMINS1 (What is the current source of your primary health insurance?)
	(109, 110), # PERSDOC3 (Do you have one person (or a group of doctors) that you think of as your personal health care provider?)
	(110, 111), # MEDCOST1 (Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?)
	(111, 112), # CHECKUP1 (About how long has it been since you last visited a doctor for a routine checkup?)
	(112, 113), # EXERANY2 (During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?)
	(113, 115), # EXRACT12 (What type of physical activity or exercise did you spend the most time doing during the past month?)
	(115, 118), # EXEROFT1 (How many times per week or per month did you take part in this activity during the past month?)
	(118, 121), # EXERHMM1 (And when you took part in this activity, for how many minutes or hours did you usually keep at it?)
	(121, 123), # EXRACT22 (What other type of physical activity gave you the next most exercise during the past month?)
	(123, 126), # EXEROFT2 (How many times per week or per month did you take part in this activity during the past month?)
	(126, 129), # EXERHMM2 (And when you took part in this activity, for how many minutes or hours did you usually keep at it?)
	(129, 132), # STRENGTH (During the past month, how many times per week or per month did you do physical activities or exercises to STRENGTHEN your muscles?   [Do NOT count aerobic activities like walking, running, or bicycling. Count activities using your own body weight like yoga, sit-ups or push-ups and those using weight machines, free weights, or elastic bands.])
	(132, 133), # BPHIGH6 (Have you ever been told by a doctor, nurse or other health professional that you have high blood pressure?  (If ´Yes´ and respondent is female, ask ´Was this only when you were pregnant?´.))
	(133, 134), # BPMEDS1 (Are you currently taking prescription medicine for your high blood pressure?)
	(134, 135), # CHOLCHK3 (About how long has it been since you last had your cholesterol checked?)
	(135, 136), # TOLDHI3 (Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?)
	(136, 137), # CHOLMED3 (Are you currently taking medicine prescribed by your doctor or other health professional for your cholesterol?)
	(137, 138), # CVDINFR4 ((Ever told) you had a heart attack, also called a myocardial infarction?)
	(138, 139), # CVDCRHD4 ((Ever told) (you had) angina or coronary heart disease?)
	(139, 140), # CVDSTRK3 ((Ever told) (you had) a stroke.)
	(140, 141), # ASTHMA3 ((Ever told) (you had) asthma?)
	(141, 142), # ASTHNOW (Do you still have asthma?)
	(142, 143), # CHCSCNC1 ((Ever told) (you had) skin cancer that is not melanoma?)
	(143, 144), # CHCOCNC1 ((Ever told) (you had) melanoma or any other types of cancer?)
	(144, 145), # CHCCOPD3 ((Ever told) (you had) C.O.P.D. (chronic obstructive pulmonary disease), emphysema or chronic bronchitis?)
	(145, 146), # ADDEPEV3 ((Ever told) (you had) a depressive disorder (including depression, major depression, dysthymia, or minor depression)?)
	(146, 147), # CHCKDNY2 (Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?)
	(147, 148), # HAVARTH4 ((Ever told) (you had) some form of arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?  (Arthritis diagnoses include: rheumatism, polymyalgia rheumatica; osteoarthritis (not osteporosis); tendonitis, bursitis, bunion, tennis elbow; carpal tunnel syndrome, tarsal tunnel syndrome; joint infection, etc.))
	(148, 149), # DIABETE4 ((Ever told) (you had) diabetes?  (If ´Yes´ and respondent is female, ask ´Was this only when you were pregnant?´. If Respondent says pre-diabetes or borderline diabetes, use response code 4.))
	(149, 151), # DIABAGE4 (How old were you when you were first told you had diabetes?)
	(185, 186), # MARITAL (Are you: (marital status))
	(186, 187), # EDUCA (What is the highest grade or year of school you completed?)
	(187, 188), # RENTHOM1 (Do you own or rent your home?)
	(196, 197), # NUMHHOL4 (Not including cell phones or numbers used for computers, fax machines or security systems, do you have more than one landline telephone number in your household?)
	(197, 198), # NUMPHON4 (How many of these landline telephone numbers are residential numbers?)
	(198, 199), # CPDEMO1C (How many cell phones do you have for your personal use?  (Last question needed for partial complete.))
	(199, 200), # VETERAN3 (Have you ever served on active duty in the United States Armed Forces, either in the regular military or in a National Guard or military reserve unit?)
	(200, 201), # EMPLOY1 (Are you currently…?)
	(201, 203), # CHILDREN (How many children less than 18 years of age live in your household?)
	(203, 205), # INCOME3 (Is your annual household income from all sources:  (If respondent refuses at any income level, code ´Refused.´))
	(205, 206), # PREGNANT (To your knowledge, are you now pregnant?)
	(206, 210), # WEIGHT2 (About how much do you weigh without shoes?  (If respondent answers in metrics, put a 9 in the first column)[Round fractions up.])
	(210, 214), # HEIGHT3 (About how tall are you without shoes?  (If respondent answers in metrics, put a 9 in the first column)[Round fractions down.])
	(214, 215), # DEAF (Are you deaf or do you have serious difficulty hearing?)
	(215, 216), # BLIND (Are you blind or do you have serious difficulty seeing, even when wearing glasses?)
	(216, 217), # DECIDE (Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?)
	(217, 218), # DIFFWALK (Do you have serious difficulty walking or climbing stairs?)
	(218, 219), # DIFFDRES (Do you have difficulty dressing or bathing?)
	(219, 220), # DIFFALON (Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor´s office or shopping?)
	(220, 222), # FALL12MN (In the past 12 months, how many times have you fallen?)
	(222, 224), # FALLINJ5 (How many of these falls caused an injury that limited your regular activities for at least a day or caused you to go to see a doctor?)
	(224, 225), # SMOKE100 (Have you smoked at least 100 cigarettes in your entire life?   [Note:  5 packs = 100 cigarettes])
	(225, 226), # SMOKDAY2 (Do you now smoke cigarettes every day, some days, or not at all?)
	(226, 227), # USENOW3 (Do you currently use chewing tobacco, snuff, or snus every day, some days, or not at all?  (Snus (Swedish for snuff) is a moist smokeless tobacco, usually sold in small pouches that are placed under the lip against the gum.))
	(227, 228), # ECIGNOW2 (Would you say you have never used e-cigarettes or other electronic vaping products in your entire life or now use them every day, use them some days, or used them in the past but do not currently use them at all?)
	(228, 231), # ALCDAY4 (During the past 30 days, how many days per week or per month did you have at least one drink of any alcoholic beverage?  (A 40 ounce beer would count as 3 drinks, or a cocktail drink with 2 shots would count as 2 drinks.))
	(231, 233), # AVEDRNK3 (One drink is equivalent to a 12-ounce beer, a 5-ounce glass of wine, or a drink with one shot of liquor. During the past 30 days, on the days when you drank, about how many drinks did you drink on the average?  (A 40 ounce beer would count as 3 drinks, or a cocktail drink with 2 shots would count as 2 drinks.))
	(233, 235), # DRNK3GE5 (Considering all types of alcoholic beverages, how many times during the past 30 days did you have 5 or more drinks for men or 4 or more drinks for women on an occasion?)
	(235, 237), # MAXDRNKS (During the past 30 days, what is the largest number of drinks you had on any occasion?)
	(237, 238), # FLUSHOT7 (During the past 12 months, have you had either flu vaccine that was sprayed in your nose or flu shot injected into your arm?)
	(238, 244), # FLSHTMY3 (During what month and year did you receive your most recent flu vaccine that was sprayed in your nose or flu shot injected into your arm?)
	(244, 245), # PNEUVAC4 (Have you ever had a pneumonia shot also known as a pneumococcal vaccine?)
	(245, 246), # SHINGLE2 (Have you ever had the shingles or zoster vaccine?)
	(246, 247), # HIVTST7 (Including fluid testing from your mouth, but not including tests you may have had for blood donation, have you ever been tested for H.I.V?)
	(247, 253), # HIVTSTD3 (Not including blood donations, in what month and year was your last H.I.V. test?  (If response is before January 1985, code ´777777´.))
	(253, 254), # SEATBELT (How often do you use seat belts when you drive or ride in a car? Would you say—)
	(254, 256), # DRNKDRI2 (During the past 30 days, how many times have you driven when you’ve had perhaps too much to drink?)
	(256, 257), # COVIDPO1 (Have you ever tested positive for COVID-19 (using a rapid point-of-care test, self-test, or laboratory test) or been told by a doctor or other health care provider that you have or had COVID-19?)
	(257, 258), # COVIDSM1 (Do you currently have symptoms lasting 3 months or longer that you did not have prior to having coronavirus or COVID-19?)
	(258, 259), # COVIDACT (Do these long-term symptoms reduce your ability to carry out day-to-day activities compared with the time before you COVID-19?)
	(259, 260), # PDIABTS1 (When was the last time you had a blood test for high blood sugar or diabetes by a doctor, nurse, or other health professional?)
	(260, 261), # PREDIAB2 (Has a doctor or other health professional ever told you that you had prediabetes or borderline diabetes?  (If “Yes” and respondent is female, ask: “Was this only when you were pregnant?”))
	(261, 262), # DIABTYPE (According to your doctor or other health professional, what type of diabetes do you have?)
	(262, 263), # INSULIN1 (Are you now taking insulin?)
	(263, 265), # CHKHEMO3 (About how many times in the past 12 months has a doctor, nurse, or other health professional checked you for A-one-C?)
	(265, 266), # EYEEXAM1 (When was the last time you had an eye exam in which the pupils were dilated, making you temporarily sensitive to bright light?)
	(266, 267), # DIABEYE1 (When was the last time a doctor, nurse or other health professional took a photo of the back of your eye with a specialized camera?)
	(267, 268), # DIABEDU1 (When was the last time you took a course or class in how to manage your diabetes yourself?)
	(268, 269), # FEETSORE (Have you ever had any sores or irritations on your feet that took more than four weeks to heal?)
	(269, 270), # ARTHEXER (Has a doctor or other health professional ever suggested physical activity or exercise to help your arthritis or joint symptoms?  (If the respondent is unclear about whether this means an increase or decrease in physical activity, this means increase.))
	(270, 271), # ARTHEDU (Have you ever taken an educational course or class to teach you how to manage problems related to your arthritis or joint symptoms?)
	(271, 272), # LMTJOIN3 (Are you now limited in any way in any of your usual activities because of arthritis or joint symptoms?)
	(272, 273), # ARTHDIS2 (Do arthritis or joint symptoms now affect whether you work, the type of work you do or the amount of work you do?)
	(273, 275), # JOINPAI2 (During the past 30 days, how bad was your joint pain on average on a scale of 0 to 10 where 0 is no pain and 10 is pain or aching as bad as it can be?)
	(275, 278), # LCSFIRST (How old were you when you first started to smoke cigarettes regularly)
	(278, 281), # LCSLAST (How old were you when you last smoked cigarettes regularly?)
	(281, 284), # LCSNUMCG (On average, when you {smoke/smoked} regularly, about how many cigarettes {do/did} you usually smoke each day?)
	(284, 285), # LCSCTSC1 (Have you ever had a CT or CAT scan of your chest area?)
	(285, 286), # LCSSCNCR (Were any of the CT or CAT scans of your chest area done mainly to check or screen for lung cancer?)
	(286, 287), # LCSCTWHN (When did you have your most recent CT or CAT scan of your chest area mainly to check or screen for lung cancer?)
	(287, 288), # HADMAM (Have you ever had a mammogram?)
	(288, 289), # HOWLONG (How long has it been since you had your last mammogram?)
	(289, 290), # CERVSCRN (Have you ever had a cervical cancer screening test?)
	(290, 291), # CRVCLCNC (How long has it been since you had your last cervical cancer screening test?)
	(291, 292), # CRVCLPAP (At your most recent cervical cancer screening, did you have a Pap test?)
	(292, 293), # CRVCLHPV (At your most recent cervical cancer screening, did you have an H.P.V. test?)
	(293, 294), # HADHYST2 (Have you had a hysterectomy?  (A hysterectomy is an operation to remove the uterus (womb).))
	(294, 295), # PSATEST1 (Have you ever had a P.S.A. test?)
	(295, 296), # PSATIME1 (About how long has it been since your most recent P.S.A. test?)
	(296, 297), # PCPSARS2 (What was the main reason you had this P.S.A. test – was it …?)
	(297, 298), # PSASUGS1 (Who first suggested (a or this) P.S.A. test: you, your doctor, or someone else?)
	(298, 299), # PCSTALK2 (When you met with a doctor, nurse, or other health professional, did they ever talk about the advantages, the disadvantages, or both advantages and disadvantages of the prostate-specific antigen or P.S.A. test?)
	(299, 300), # HADSIGM4 (Colonoscopy and sigmoidoscopy are exams to check for colon cancer. Have you ever had either of these exams?)
	(300, 301), # COLNSIGM (Have you had a colonoscopy, a sigmoidoscopy, or both?)
	(301, 302), # COLNTES1 (How long has it been since your most recent colonoscopy?)
	(302, 303), # SIGMTES1 (How long has it been since your most recent sigmoidoscopy?)
	(303, 304), # LASTSIG4 (How long has it been since your most recent colonoscopy or sigmoidoscopy?)
	(304, 305), # COLNCNCR (Have you ever had any other kind of test for colorectal cancer, such as virtual colonoscopy, CT colonography, blood stool test, FIT DNA, or Cologuard test?)
	(305, 306), # VIRCOLO1 (A virtual colonoscopy uses a series of X-rays to take pictures of inside the colon.  Have you ever had a virtual colonoscopy?)
	(306, 307), # VCLNTES2 (When was your most recent CT colonography or virtual colonoscopy?)
	(307, 308), # SMALSTOL (One stool test uses a special kit to obtain a small amount of stool at home and returns the kit to the doctor or the lab. Have you ever had this test?)
	(308, 309), # STOLTEST (How long has it been since you had this test?)
	(309, 310), # STOOLDN2 (Another stool test uses a special kit to obtain an entire bowel movement at home and returns the kit to a lab.   Have you ever had this test?)
	(310, 311), # BLDSTFIT (Was the blood stool or FIT (you reported earlier) conducted as part of a Cologuard test?)
	(311, 312), # SDNATES1 (How long has it been since you had this test?)
	(312, 313), # CNCRDIFF (How many different types of cancer have you had?)
	(313, 315), # CNCRAGE (At what age were you told that you had cancer?  (If Response = 2 (Two) or 3 (Three or more), ask: “At what age was your first diagnosis of cancer?”))
	(315, 317), # CNCRTYP2 (What kind of cancer is it?)
	(317, 318), # CSRVTRT3 (Are you currently receiving treatment for cancer?)
	(318, 320), # CSRVDOC1 (What type of doctor provides the majority of your health care? Is it a….)
	(320, 321), # CSRVSUM (Did any doctor, nurse, or other health professional ever give you a written summary of all the cancer treatments that you received?)
	(321, 322), # CSRVRTRN (Have you ever received instructions from a doctor, nurse, or other health professional about where you should return or who you should see for routine cancer check-ups after completing treatment for cancer?)
	(322, 323), # CSRVINST (Were these instructions written down or printed on paper for you?)
	(323, 324), # CSRVINSR (With your most recent diagnosis of cancer, did you have health insurance that paid for all or part of your cancer treatment?  (“Health insurance” also includes Medicare, Medicaid, or other types of state health programs.))
	(324, 325), # CSRVDEIN (Were you ever denied health insurance or life insurance coverage because of your cancer?)
	(325, 326), # CSRVCLIN (Did you participate in a clinical trial as part of your cancer treatment?)
	(326, 327), # CSRVPAIN (Do you currently have physical pain caused by your cancer or cancer treatment?)
	(327, 328), # CSRVCTL2 (Would you say your pain is currently under control…?)
	(328, 331), # INDORTAN (Not including spray-on tans, during the past 12 months, how many times have you used an indoor tanning device such as a sunlamp, tanning bed, or booth?)
	(331, 334), # NUMBURN3 (During the past 12 months, how many times have you had a sunburn?)
	(334, 335), # SUNPRTCT (When you go outside on a warm sunny day for more than one hour, how often do you protect yourself from the sun? Is that….)
	(335, 337), # WKDAYOUT (On weekdays, in the summer, how long are you outside per day between 10am and 4pm?)
	(337, 339), # WKENDOUT (On weekends in the summer, how long are you outside each day between 10am and 4pm?)
	(339, 340), # CIMEMLO1 (During the past 12 months, have you experienced difficulties with thinking or memory that are happening more often or are getting worse?)
	(340, 341), # CDWORRY (Are you worried about these difficulties with thinking or memory?)
	(341, 342), # CDDISCU1 (Have you or anyone else discussed your difficulties with thinking or memory with a health care provider?)
	(342, 343), # CDHOUS1 (During the past 12 months, have your difficulties with thinking or memory interfered with day-to-day activities, such as managing medications, paying bills, or keeping track of appointments?)
	(343, 344), # CDSOCIA1 (During the past 12 months, have your difficulties with thinking or memory interfered with your ability to work or volunteer?)
	(344, 345), # CAREGIV1 (During the past 30 days, did you provide regular care or assistance to a friend or family member who has a health problem or disability?)
	(345, 347), # CRGVREL4 (What is his or her relationship to you?)
	(347, 348), # CRGVLNG1 (For how long have you provided care for that person?)
	(348, 349), # CRGVHRS1 (In an average week, how many hours do you provide care or assistance?)
	(349, 351), # CRGVPRB3 (What is the main health problem, long-term illness, or disability that the person you care for has?)
	(351, 352), # CRGVALZD (Does the person you care for also have Alzheimer´s disease, dementia or other cognitive impairment disorder?)
	(352, 353), # CRGVPER1 (In the past 30 days, did you provide care for this person by managing personal care such as giving medications, feeding, dressing, or bathing?)
	(353, 354), # CRGVHOU1 (In the past 30 days, did you provide care for this person by managing household tasks such as cleaning, managing money, or preparing meals?)
	(354, 355), # CRGVEXPT (In the next 2 years, do you expect to provide care or assistance to a friend or family member who has a health problem or disability?)
	(355, 357), # LASTSMK2 (How long has it been since you last smoked a cigarette, even one or two puffs?)
	(357, 358), # STOPSMK2 (During the past 12 months, have you stopped smoking for one day or longer because you were trying to quit smoking?)
	(358, 359), # MENTCIGS (Currently, when you smoke cigarettes, do you usually smoke menthol cigarettes?)
	(359, 360), # MENTECIG (Currently, when you use e-cigarettes, do you usually use menthol e-cigarettes?)
	(360, 361), # HEATTBCO (Before today, have you heard of heated tobacco products?)
	(361, 362), # FIREARM5 (Are any firearms now kept in or around your home?)
	(362, 363), # GUNLOAD (Are any of these firearms now loaded?)
	(363, 364), # LOADULK2 (Are any of these loaded firearms also unlocked?)
	(564, 565), # HASYMP1 ((Do you think) pain or discomfort in the jaw, neck, or back (are symptoms of a heart attack)?)
	(565, 566), # HASYMP2 ((Do you think) feeling weak, lightheaded, or faint (are symptoms of a heart attack)?)
	(566, 567), # HASYMP3 ((Do you think) chest pain or discomfort (are symptoms of a heart attack)?)
	(567, 568), # HASYMP4 ((Do you think) sudden trouble seeing in one or both eyes (are symptoms of a heart attack)?)
	(568, 569), # HASYMP5 ((Do you think) pain or discomfort in the arms or shoulder (are symptoms of a heart attack)?)
	(569, 570), # HASYMP6 ((Do you think) shortness of breath (is a symptom of a heart attack)?)
	(570, 571), # STRSYMP1 ((Do you think) sudden confusion or trouble speaking (are symptoms of a stroke?))
	(571, 572), # STRSYMP2 ((Do you think) sudden numbness or weakness of face, arm, or leg, especially on one side (are symptoms of a stroke?))
	(572, 573), # STRSYMP3 ((Do you think) sudden trouble seeing in one or both eyes (is a symptom of a stroke?))
	(573, 574), # STRSYMP4 ((Do you think) sudden chest pain or discomfort (are symptoms of a stroke?))
	(574, 575), # STRSYMP5 ((Do you think) sudden trouble walking, dizziness, or loss of balance (are symptoms of a stroke?))
	(575, 576), # STRSYMP6 ((Do you think) severe headache with no known cause (is a symptom of a stroke?))
	(576, 577), # FIRSTAID (If you thought someone was having a heart attack or a stroke, what is the first thing you would do?)
	(577, 578), # ASPIRIN (How often do you take an aspirin to prevent or control heart disease, heart attacks or stroke?  Would you say….)
	(578, 579), # BIRTHSEX (What was your sex at birth? Was it male or female?)
	(579, 580), # SOMALE (Which of the following best represents how you think of yourself?)
	(580, 581), # SOFEMALE (Which of the following best represents how you think of yourself?)
	(581, 582), # TRNSGNDR (Do you consider yourself to be transgender?  (If yes, ask “Do you consider yourself to be male-to-female, female-to-male, or gender non-conforming?))
	(582, 584), # MARIJAN1 (During the past 30 days, on how many days did you use marijuana or cannabis?)
	(584, 585), # MARJSMOK (During the past 30 days, did you smoke it (for example, in a joint, bong, pipe, or blunt)?)
	(585, 586), # MARJEAT (Did you eat it or drink it (for example, in brownies, cakes, cookies, or candy, or in tea, cola, or alcohol)?)
	(586, 587), # MARJVAPE (Did you vaporize it (for example, in an e-cigarette-like vaporizer or another vaporizing device))
	(587, 588), # MARJDAB (Did you dab it (for example, using a dabbing rig, knife, or dab pen)?)
	(588, 589), # MARJOTHR (Did you use it in some other way?)
	(590, 591), # ACEDEPRS (Did you live with anyone who was depressed, mentally ill, or suicidal?)
	(591, 592), # ACEDRINK (Did you live with anyone who was a problem drinker or alcoholic?)
	(592, 593), # ACEDRUGS (Did you live with anyone who used illegal street drugs or who abused prescription medications?)
	(593, 594), # ACEPRISN (Did you live with anyone who served time or was sentenced to serve time in a prison, jail, or other correctional facility?)
	(594, 595), # ACEDIVRC (Were your parents separated or divorced?)
	(595, 596), # ACEPUNCH (How often did your parents or adults in your home ever slap, hit, kick, punch or beat each other up?)
	(596, 597), # ACEHURT1 (Not including spanking, (before age 18), how often did a parent or adult in your home ever hit, beat, kick, or physically hurt you in any way? Was it—)
	(597, 598), # ACESWEAR (How often did a parent or adult in your home ever swear at you, insult you, or put you down?)
	(598, 599), # ACETOUCH (How often did anyone at least 5 years older than you or an adult, ever touch you sexually?)
	(599, 600), # ACETTHEM (How often did anyone at least 5 years older than you or an adult, try to make you touch them sexually?)
	(600, 601), # ACEHVSEX (How often did anyone at least 5 years older than you or an adult, force you to have sex?)
	(601, 602), # ACEADSAF (For how much of your childhood was there an adult in your household who made you feel safe and protected? Would you say never, a little of the time, some of the time, most of the time, or all of the time?)
	(602, 603), # ACEADNED (For how much of your childhood was there an adult in your household who tried hard to make sure your basic needs were met? Would you say never, a little of the time, some of the time, most of the time, or all of the time?)
	(603, 605), # IMFVPLA4 (At what kind of place did you get your last flu shot or vaccine?)
	(605, 606), # HPVADVC4 (Have you ever had an H.P.V. vaccination?)
	(606, 608), # HPVADSHT (How many HPV shots did you receive?)
	(608, 609), # TETANUS1 (Have you received a tetanus shot in the past 10 years?  (If yes, ask: “Was this Tdap, the tetanus shot that also has pertussis or whooping cough vaccine?”))
	(609, 610), # COVIDVA1 (Have you received at least one dose of a  COVID-19 vaccination?)
	(610, 611), # COVACGE1 (Would you say you will definitely get a vaccine, will probably get a vaccine, will probably not get a vaccine, will definitely not get a vaccine, or are you not sure?)
	(611, 612), # COVIDNU2 (How many COVID-19 vaccinations have you received?)
	(612, 613), # LSATISFY (In general, how satisfied are you with your life?)
	(613, 614), # EMTSUPRT (How often do you get the social and emotional support you need?)
	(614, 615), # SDLONELY (How often do you feel lonely?  Is it…)
	(615, 616), # SDHEMPLY (In the past 12 months have you lost employment or had hours reduced?)
	(616, 617), # FOODSTMP (During the past 12 months, have you received food stamps, also called SNAP, the Supplemental Nutrition Assistance Program on an EBT card?)
	(617, 618), # SDHFOOD1 (During the past 12 months how often did the food that you bought not last, and you didn’t have money to get more? Was that…)
	(618, 619), # SDHBILLS (During the last 12 months, was there a time when you were not able to pay your mortgage, rent or utility bills?)
	(619, 620), # SDHUTILS (During the last 12 months was there a time when an electric, gas, oil, or water company threatened to shut off services?)
	(620, 621), # SDHTRNSP (During the past 12 months has a lack of reliable transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living?)
	(621, 622), # SDHSTRE1 (Within the last 30 days, how often have you felt this kind of stress?)
	(622, 624), # RRCLASS3 (How do other people usually classify you in this country? Would you say White, Black or African American, Hispanic or Latino, Asian, Native Hawaiian or Other Pacific Islander, American Indian or Alaska Native, or some other group?)
	(624, 625), # RRCOGNT2 (How often do you think about your race? Would you say never, once a year, once a month, once a week, once a day, once an hour, or constantly?)
	(625, 626), # RRTREAT (Within the past 12 months, do you feel that in general you were treated worse than, the same as, or better than people of other races?)
	(626, 627), # RRATWRK2 (Within the past 12 months at work, do you feel you were treated worse than, the same as, or better than people of other races?)
	(627, 628), # RRHCARE4 (Within the past 12 months when seeking health care, do you feel your experiences were worse than, the same as, or better than for people of other races?)
	(628, 629), # RRPHYSM2 (Within the past 30 days, have you experienced any physical symptoms, for example, a headache, an upset stomach, tensing of your muscles, or a pounding heart, as a result of how you were treated based on your race?)
	(635, 636), # RCSGEND1 (Is the child a boy or a girl?)
	(636, 637), # RCSXBRTH (What was the child´s sex on their original birth certificate?)
	(669, 670), # RCSRLTN2 (How are you related to the child?)
	(670, 671), # CASTHDX2 (Has a doctor, nurse or other health professional EVER said that the child has asthma?)
	(671, 672), # CASTHNO2 (Does the child still have asthma?)
	(676, 678), # QSTVER (Questionnaire Version Identifier)
	(678, 680), # QSTLANG (Language identifier)
	(1401, 1402), # _METSTAT (Metropolitan Status)
	(1402, 1403), # _URBSTAT (Urban/Rural Status)
	(1408, 1409), # MSCODE (Metropolitan Status Code)
	(1409, 1415), # _STSTR (Sample Design Stratification Variable  (Prior to 2011:  _STSTR is a five digit number that combines the values for _STATE (first two characters), _GEOSTR (third and fourth character), and _DENSTR2 (final character).))
	(1415, 1425), # _STRWT (Stratum weight  (Number of records in a stratum (NRECSTR) divided by the number of records selected (NRECSEL).))
	(1445, 1455), # _RAWRAKE (Raw weighting factor used in raking  (Number of adults in the household (NUMADULT, maximum of 5) divided by the imputed number of phones (_IMPNPH, maximum of 3).))
	(1455, 1465), # _WT2RAKE (Design weight used in raking  (Stratum weight (_STRWT) multiplied by the raw weighting factor (_RAWRAKE).))
	(1470, 1472), # _IMPRACE (Imputed race/ethnicity value  (This value is the reported race/ethnicity or an imputed race/ethnicity, if the respondent refused to give a race/ethnicity. The value of the imputed race/ethnicity will be the most common race/ethnicity response for that region of the state))
	(1481, 1482), # _CHISPNC (Child Hispanic, Latino/a, or Spanish origin calculated variable)
	(1538, 1540), # _CRACE1 (Child multiracial race categorization)
	(1566, 1567), # CAGEG (Four level child age)
	(1582, 1592), # _CLLCPWT (Final child weight: Land-line and Cell-Phone data  (Raking derived weight))
	(1679, 1680), # _DUALUSE (Dual Phone Use Categories)
	(1680, 1690), # _DUALCOR (Dual phone use correction factor)
	(1690, 1700), # _LLCPWT2 (Truncated design weight used in adult combined land line and cell phone raking)
	(1748, 1758), # _LLCPWT (Final weight assigned to each  respondent: Land-line and cell-phone data  (Raking derived weight))
	(1896, 1897), # _RFHLTH (Adults with good or better health)
	(1897, 1898), # _PHYS14D (3 level not good physical health status: 0 days, 1-13 days, 14-30 days)
	(1898, 1899), # _MENT14D (3 level not good mental health status: 0 days, 1-13 days, 14-30 days)
	(1899, 1900), # _HLTHPL1 (Adults who had some form of health insurance)
	(1900, 1901), # _HCVU653 (Respondents aged 18-64 who have any form of health insurance)
	(1901, 1902), # _TOTINDA (Adults who reported doing physical activity or exercise during the past 30 days other than their regular job)
	(1902, 1905), # METVL12_ (Activity MET Value for First Activity)
	(1905, 1908), # METVL22_ (Activity MET Value for Second Activity)
	(1908, 1913), # MAXVO21_ (Estimated Age-Gender Specific Maximum Oxygen Consumption)
	(1913, 1918), # FC601_ (Estimated Functional Capacity)
	(1918, 1919), # ACTIN13_ (Estimated Activity Intensity for First Activity)
	(1919, 1920), # ACTIN23_ (Estimated Activity Intensity for Second Activity)
	(1920, 1923), # PADUR1_ (Minutes of First Activity)
	(1923, 1926), # PADUR2_ (Minutes of Second Activity)
	(1926, 1931), # PAFREQ1_ (Physical Activity Frequency per Week for First Activity)
	(1931, 1936), # PAFREQ2_ (Physical Activity Frequency per Week for Second Activity)
	(1936, 1941), # _MINAC12 (Minutes of Physical Activity per week for First Activity)
	(1941, 1946), # _MINAC22 (Minutes of Physical Activity per week for Second Activity)
	(1946, 1951), # STRFREQ_ (Strength Activity Frequency per Week)
	(1951, 1952), # PAMISS3_ (Missing Physical Activity Data)
	(1952, 1957), # PAMIN13_ (Minutes of Physical Activity per week for First Activity)
	(1957, 1962), # PAMIN23_ (Minutes of Physical Activity per week for Second Activity)
	(1962, 1967), # PA3MIN_ (Minutes of total Physical Activity per week)
	(1967, 1972), # PAVIG13_ (Minutes of Vigorous Physical Activity per week for First Activity)
	(1972, 1977), # PAVIG23_ (Minutes of Vigorous Physical Activity per week for Second Activity)
	(1977, 1982), # PA3VIGM_ (Minutes of total Vigorous Physical Activity per week)
	(1982, 1983), # _PACAT3 (Physical Activity Categories)
	(1983, 1984), # _PAINDX3 (Physical Activity Index)
	(1984, 1985), # _PA150R4 (Adults that participated in 150 minutes (or vigorous equivalent minutes) of physical activity per week.)
	(1985, 1986), # _PA300R4 (Adults that participated in greater than 300 minutes  (or vigorous equivalent minutes) of physical activity per week.)
	(1986, 1987), # _PA30023 (Adults that participated in greater than 300 minutes  (or vigorous equivalent minutes) of physical activity per week (2-levels).)
	(1987, 1988), # _PASTRNG (Muscle Strengthening Recommendation)
	(1988, 1989), # _PAREC3 (Aerobic and Strengthening Guideline)
	(1989, 1990), # _PASTAE3 (Aerobic and Strengthening (2-level))
	(1990, 1991), # _RFHYPE6 (Adults who have been told they have high blood pressure by a doctor, nurse, or other health professional)
	(1991, 1992), # _CHOLCH3 (Cholesterol check within past five years)
	(1992, 1993), # _RFCHOL3 (Adults who have had their cholesterol checked and have been told by a doctor, nurse, or other health professional that it was high)
	(1993, 1994), # _MICHD (Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI))
	(1994, 1995), # _LTASTH1 (Adults who have ever been told they have asthma)
	(1995, 1996), # _CASTHM1 (Adults who have been told they currently have asthma)
	(1996, 1997), # _ASTHMS1 (Computed asthma status)
	(1997, 1998), # _DRDXAR2 (Respondents who have had a doctor diagnose them as having some form of arthritis)
	(2054, 2056), # _MRACE1 (Calculated multiracial race categorization)
	(2058, 2059), # _HISPANC (Hispanic, Latino/a, or Spanish origin calculated variable)
	(2059, 2060), # _RACE (Race/ethnicity categories)
	(2060, 2061), # _RACEG21 (White non-Hispanic race group)
	(2061, 2062), # _RACEGR3 (Five-level race/ethnicity category)
	(2062, 2063), # _RACEPRV (Computed race groups used for internet prevalence tables)
	(2063, 2064), # _SEX (Calculated sex variable)
	(2064, 2066), # _AGEG5YR (Fourteen-level age category)
	(2066, 2067), # _AGE65YR (Two-level age category)
	(2067, 2069), # _AGE80 (Imputed Age value collapsed above 80)
	(2069, 2070), # _AGE_G (Six-level imputed age category)
	(2070, 2073), # HTIN4 (Reported height in inches)
	(2073, 2076), # HTM4 (Reported height in meters)
	(2076, 2081), # WTKG3 (Reported weight in kilograms)
	(2081, 2085), # _BMI5 (Body Mass Index (BMI))
	(2085, 2086), # _BMI5CAT (Four-categories of Body Mass Index (BMI))
	(2086, 2087), # _RFBMI5 (Adults who have a body mass index greater than 25.00 (Overweight or Obese))
	(2087, 2088), # _CHLDCNT (Number of children in household)
	(2088, 2089), # _EDUCAG (Level of education completed)
	(2089, 2090), # _INCOMG1 (Income categories)
	(2090, 2091), # _SMOKER3 (Four-level smoker status:  Everyday smoker, Someday smoker, Former smoker, Non-smoker)
	(2091, 2092), # _RFSMOK3 (Adults who are current smokers)
	(2092, 2093), # _CURECI2 (Adults who are current e-cigarette users)
	(2093, 2094), # DRNKANY6 (Adults who reported having had at least one drink of alcohol in the past 30 days.)
	(2094, 2097), # DROCDY4_ (Drink-occasions-per-day)
	(2097, 2098), # _RFBING6 (Binge drinkers (males having five or more drinks on one occasion, females having four or more drinks on one occasion))
	(2098, 2103), # _DRNKWK2 (Calculated total number of alcoholic beverages consumed per week)
	(2103, 2104), # _RFDRHV8 (Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week))
	(2104, 2105), # _FLSHOT7 (Adults aged 65+ who have had a flu shot within the past year)
	(2105, 2106), # _PNEUMO3 (Adults aged 65+ who have ever had a pneumonia vaccination)
	(2106, 2107), # _AIDTST4 (Adults who have ever been tested for HIV)
	(2107, 2108), # _RFSEAT2 (Always or Nearly Always Wear Seat Belts Calculated Variable)
	(2108, 2109), # _RFSEAT3 (Always Wear Seat Belts Calculated Variable)
	(2109, 2110), # _DRNKDRV (Drinking and Driving  (Reported having driven at least once when perhaps had too much to drink))
]


column_names = [
	'_STATE',
	'FMONTH',
	'IDATE',
	'IMONTH',
	'IDAY',
	'IYEAR',
	'DISPCODE',
	'SEQNO',
	'_PSU',
	'CTELENM1',
	'PVTRESD1',
	'COLGHOUS',
	'STATERE1',
	'CELPHON1',
	'LADULT1',
	'NUMADULT',
	'RESPSLC1',
	'LANDSEX2',
	'LNDSXBRT',
	'SAFETIME',
	'CTELNUM1',
	'CELLFON5',
	'CADULT1',
	'CELLSEX2',
	'CELSXBRT',
	'PVTRESD3',
	'CCLGHOUS',
	'CSTATE1',
	'LANDLINE',
	'HHADULT',
	'SEXVAR',
	'GENHLTH',
	'PHYSHLTH',
	'MENTHLTH',
	'POORHLTH',
	'PRIMINS1',
	'PERSDOC3',
	'MEDCOST1',
	'CHECKUP1',
	'EXERANY2',
	'EXRACT12',
	'EXEROFT1',
	'EXERHMM1',
	'EXRACT22',
	'EXEROFT2',
	'EXERHMM2',
	'STRENGTH',
	'BPHIGH6',
	'BPMEDS1',
	'CHOLCHK3',
	'TOLDHI3',
	'CHOLMED3',
	'CVDINFR4',
	'CVDCRHD4',
	'CVDSTRK3',
	'ASTHMA3',
	'ASTHNOW',
	'CHCSCNC1',
	'CHCOCNC1',
	'CHCCOPD3',
	'ADDEPEV3',
	'CHCKDNY2',
	'HAVARTH4',
	'DIABETE4',
	'DIABAGE4',
	'MARITAL',
	'EDUCA',
	'RENTHOM1',
	'NUMHHOL4',
	'NUMPHON4',
	'CPDEMO1C',
	'VETERAN3',
	'EMPLOY1',
	'CHILDREN',
	'INCOME3',
	'PREGNANT',
	'WEIGHT2',
	'HEIGHT3',
	'DEAF',
	'BLIND',
	'DECIDE',
	'DIFFWALK',
	'DIFFDRES',
	'DIFFALON',
	'FALL12MN',
	'FALLINJ5',
	'SMOKE100',
	'SMOKDAY2',
	'USENOW3',
	'ECIGNOW2',
	'ALCDAY4',
	'AVEDRNK3',
	'DRNK3GE5',
	'MAXDRNKS',
	'FLUSHOT7',
	'FLSHTMY3',
	'PNEUVAC4',
	'SHINGLE2',
	'HIVTST7',
	'HIVTSTD3',
	'SEATBELT',
	'DRNKDRI2',
	'COVIDPO1',
	'COVIDSM1',
	'COVIDACT',
	'PDIABTS1',
	'PREDIAB2',
	'DIABTYPE',
	'INSULIN1',
	'CHKHEMO3',
	'EYEEXAM1',
	'DIABEYE1',
	'DIABEDU1',
	'FEETSORE',
	'ARTHEXER',
	'ARTHEDU',
	'LMTJOIN3',
	'ARTHDIS2',
	'JOINPAI2',
	'LCSFIRST',
	'LCSLAST',
	'LCSNUMCG',
	'LCSCTSC1',
	'LCSSCNCR',
	'LCSCTWHN',
	'HADMAM',
	'HOWLONG',
	'CERVSCRN',
	'CRVCLCNC',
	'CRVCLPAP',
	'CRVCLHPV',
	'HADHYST2',
	'PSATEST1',
	'PSATIME1',
	'PCPSARS2',
	'PSASUGS1',
	'PCSTALK2',
	'HADSIGM4',
	'COLNSIGM',
	'COLNTES1',
	'SIGMTES1',
	'LASTSIG4',
	'COLNCNCR',
	'VIRCOLO1',
	'VCLNTES2',
	'SMALSTOL',
	'STOLTEST',
	'STOOLDN2',
	'BLDSTFIT',
	'SDNATES1',
	'CNCRDIFF',
	'CNCRAGE',
	'CNCRTYP2',
	'CSRVTRT3',
	'CSRVDOC1',
	'CSRVSUM',
	'CSRVRTRN',
	'CSRVINST',
	'CSRVINSR',
	'CSRVDEIN',
	'CSRVCLIN',
	'CSRVPAIN',
	'CSRVCTL2',
	'INDORTAN',
	'NUMBURN3',
	'SUNPRTCT',
	'WKDAYOUT',
	'WKENDOUT',
	'CIMEMLO1',
	'CDWORRY',
	'CDDISCU1',
	'CDHOUS1',
	'CDSOCIA1',
	'CAREGIV1',
	'CRGVREL4',
	'CRGVLNG1',
	'CRGVHRS1',
	'CRGVPRB3',
	'CRGVALZD',
	'CRGVPER1',
	'CRGVHOU1',
	'CRGVEXPT',
	'LASTSMK2',
	'STOPSMK2',
	'MENTCIGS',
	'MENTECIG',
	'HEATTBCO',
	'FIREARM5',
	'GUNLOAD',
	'LOADULK2',
	'HASYMP1',
	'HASYMP2',
	'HASYMP3',
	'HASYMP4',
	'HASYMP5',
	'HASYMP6',
	'STRSYMP1',
	'STRSYMP2',
	'STRSYMP3',
	'STRSYMP4',
	'STRSYMP5',
	'STRSYMP6',
	'FIRSTAID',
	'ASPIRIN',
	'BIRTHSEX',
	'SOMALE',
	'SOFEMALE',
	'TRNSGNDR',
	'MARIJAN1',
	'MARJSMOK',
	'MARJEAT',
	'MARJVAPE',
	'MARJDAB',
	'MARJOTHR',
	'ACEDEPRS',
	'ACEDRINK',
	'ACEDRUGS',
	'ACEPRISN',
	'ACEDIVRC',
	'ACEPUNCH',
	'ACEHURT1',
	'ACESWEAR',
	'ACETOUCH',
	'ACETTHEM',
	'ACEHVSEX',
	'ACEADSAF',
	'ACEADNED',
	'IMFVPLA4',
	'HPVADVC4',
	'HPVADSHT',
	'TETANUS1',
	'COVIDVA1',
	'COVACGE1',
	'COVIDNU2',
	'LSATISFY',
	'EMTSUPRT',
	'SDLONELY',
	'SDHEMPLY',
	'FOODSTMP',
	'SDHFOOD1',
	'SDHBILLS',
	'SDHUTILS',
	'SDHTRNSP',
	'SDHSTRE1',
	'RRCLASS3',
	'RRCOGNT2',
	'RRTREAT',
	'RRATWRK2',
	'RRHCARE4',
	'RRPHYSM2',
	'RCSGEND1',
	'RCSXBRTH',
	'RCSRLTN2',
	'CASTHDX2',
	'CASTHNO2',
	'QSTVER',
	'QSTLANG',
	'_METSTAT',
	'_URBSTAT',
	'MSCODE',
	'_STSTR',
	'_STRWT',
	'_RAWRAKE',
	'_WT2RAKE',
	'_IMPRACE',
	'_CHISPNC',
	'_CRACE1',
	'CAGEG',
	'_CLLCPWT',
	'_DUALUSE',
	'_DUALCOR',
	'_LLCPWT2',
	'_LLCPWT',
	'_RFHLTH',
	'_PHYS14D',
	'_MENT14D',
	'_HLTHPL1',
	'_HCVU653',
	'_TOTINDA',
	'METVL12_',
	'METVL22_',
	'MAXVO21_',
	'FC601_',
	'ACTIN13_',
	'ACTIN23_',
	'PADUR1_',
	'PADUR2_',
	'PAFREQ1_',
	'PAFREQ2_',
	'_MINAC12',
	'_MINAC22',
	'STRFREQ_',
	'PAMISS3_',
	'PAMIN13_',
	'PAMIN23_',
	'PA3MIN_',
	'PAVIG13_',
	'PAVIG23_',
	'PA3VIGM_',
	'_PACAT3',
	'_PAINDX3',
	'_PA150R4',
	'_PA300R4',
	'_PA30023',
	'_PASTRNG',
	'_PAREC3',
	'_PASTAE3',
	'_RFHYPE6',
	'_CHOLCH3',
	'_RFCHOL3',
	'_MICHD',
	'_LTASTH1',
	'_CASTHM1',
	'_ASTHMS1',
	'_DRDXAR2',
	'_MRACE1',
	'_HISPANC',
	'_RACE',
	'_RACEG21',
	'_RACEGR3',
	'_RACEPRV',
	'_SEX',
	'_AGEG5YR',
	'_AGE65YR',
	'_AGE80',
	'_AGE_G',
	'HTIN4',
	'HTM4',
	'WTKG3',
	'_BMI5',
	'_BMI5CAT',
	'_RFBMI5',
	'_CHLDCNT',
	'_EDUCAG',
	'_INCOMG1',
	'_SMOKER3',
	'_RFSMOK3',
	'_CURECI2',
	'DRNKANY6',
	'DROCDY4_',
	'_RFBING6',
	'_DRNKWK2',
	'_RFDRHV8',
	'_FLSHOT7',
	'_PNEUMO3',
	'_AIDTST4',
	'_RFSEAT2',
	'_RFSEAT3',
	'_DRNKDRV',
]

# Read the fixed-width formatted file
df = pd.read_fwf('LLCP2023.ASC', colspecs=colspecs, names=column_names)
