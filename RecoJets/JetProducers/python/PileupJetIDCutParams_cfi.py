import FWCore.ParameterSet.Config as cms

###########################################################
## Working points for the 102X training
###########################################################
full_102x_chs_wp  = cms.PSet(
    #8 Eta Categories  0-1.0 1.0-1.5 1.5-2.0 2.0-2.5 2.5-2.6 2.6-2.7 2.7-3.0 3.0-5.0

    #Tight Id: Background Eff - {Eta 0-3.0: 1%} {Eta 3.0-5.0: 20%}
    Pt010_Tight    = cms.vdouble(0.925,  0.924,  0.924,  0.924,  0.924,  0.875,  0.827,  0.160),
    Pt1020_Tight   = cms.vdouble(0.925,  0.924,  0.924,  0.924,  0.924,  0.875,  0.827,  0.160),
    Pt2030_Tight   = cms.vdouble(0.925,  0.924,  0.924,  0.924,  0.924,  0.875,  0.827,  0.160),
    Pt3050_Tight   = cms.vdouble(0.925,  0.924,  0.924,  0.924,  0.924,  0.875,  0.827,  0.160),
    #Signal Eff                  79.0 %, 76.5 %, 73.5 %, 73.5 %, 68.9 %, 65.0 %, 43.3 %, 49.0 %

    #Medium Id: Background Eff - {Eta 0-3.0: 5%} {Eta 3.0-5.0: 30%}
    Pt010_Medium   = cms.vdouble(-0.125, -0.025,  0.075,  0.076,  0.229,  0.382,  0.485,  0.035),
    Pt1020_Medium  = cms.vdouble(-0.125, -0.025,  0.075,  0.076,  0.229,  0.382,  0.485,  0.035),
    Pt2030_Medium  = cms.vdouble(-0.125, -0.025,  0.075,  0.076,  0.229,  0.382,  0.485,  0.035),
    Pt3050_Medium  = cms.vdouble(-0.125, -0.025,  0.075,  0.076,  0.229,  0.382,  0.485,  0.035),
    #Signal Eff                  97.4 %, 96.6 %, 95.9 %, 95.1 %, 90.7 %, 82.9 %, 62.5 %, 60.9 %

    #Loose Id: Background Eff - {Eta 0-3.0: 10%} {Eta 3.0-5.0: 40%}
    Pt010_Loose    = cms.vdouble(-0.774, -0.724, -0.674, -0.622, -0.367, -0.112,  0.192, -0.049),
    Pt1020_Loose   = cms.vdouble(-0.774, -0.724, -0.674, -0.622, -0.367, -0.112,  0.192, -0.049),
    Pt2030_Loose   = cms.vdouble(-0.774, -0.724, -0.674, -0.622, -0.367, -0.112,  0.192, -0.049),
    Pt3050_Loose   = cms.vdouble(-0.774, -0.724, -0.674, -0.622, -0.367, -0.112,  0.192, -0.049)
    #Signal Eff                  98.9 %, 98.5 %, 98.2 %, 97.7 %, 95.1 %, 89.6 %, 72.1 %, 68.8 %
)

###########################################################
## Working points for the 94X training
###########################################################
full_94x_chs_wp  = cms.PSet(
    #8 Eta Categories  0-1.0 1.0-1.5 1.5-2.0 2.0-2.5 2.5-2.6 2.6-2.7 2.7-3.0 3.0-5.0

    #Tight Id: Background Eff - {Eta 0-3.0: 1%} {Eta 3.0-5.0: 20%}
    Pt010_Tight    = cms.vdouble(0.875,  0.875,  0.875,  0.925,  0.876,  0.876,  0.830,  0.072),
    Pt1020_Tight   = cms.vdouble(0.875,  0.875,  0.875,  0.925,  0.876,  0.876,  0.830,  0.072),
    Pt2030_Tight   = cms.vdouble(0.875,  0.875,  0.875,  0.925,  0.876,  0.876,  0.830,  0.072),
    Pt3050_Tight   = cms.vdouble(0.875,  0.875,  0.875,  0.925,  0.876,  0.876,  0.830,  0.072),
    #Signal Eff                  83.5 %, 81.9 %, 79.5 %, 71.6 %, 71.4 %, 63.2 %, 41.9 %, 55.0 %

    #Medium Id: Background Eff - {Eta 0-3.0: 5%} {Eta 3.0-5.0: 30%}
    Pt010_Medium   = cms.vdouble(-0.123, -0.073,  0.027,  0.177,  0.230,  0.383,  0.493, -0.015),
    Pt1020_Medium  = cms.vdouble(-0.123, -0.073,  0.027,  0.177,  0.230,  0.383,  0.493, -0.015),
    Pt2030_Medium  = cms.vdouble(-0.123, -0.073,  0.027,  0.177,  0.230,  0.383,  0.493, -0.015),
    Pt3050_Medium  = cms.vdouble(-0.123, -0.073,  0.027,  0.177,  0.230,  0.383,  0.493, -0.015),
    #Signal Eff                  95.4 %, 94.5 %, 93.5 %, 92.4 %, 89.2 %, 82.1 %, 61.3 %, 62.7 %

    #Loose Id: Background Eff - {Eta 0-3.0: 10%} {Eta 3.0-5.0: 40%}
    Pt010_Loose    = cms.vdouble(-0.622, -0.573, -0.521, -0.421, -0.267, -0.110,  0.204, -0.101),
    Pt1020_Loose   = cms.vdouble(-0.622, -0.573, -0.521, -0.421, -0.267, -0.110,  0.204, -0.101),
    Pt2030_Loose   = cms.vdouble(-0.622, -0.573, -0.521, -0.421, -0.267, -0.110,  0.204, -0.101),
    Pt3050_Loose   = cms.vdouble(-0.622, -0.573, -0.521, -0.421, -0.267, -0.110,  0.204, -0.101)
    #Signal Eff                  97.4 %, 96.8 %, 96.2 %, 95.8 %, 93.8 %, 89.0 %, 70.2 %, 70.8 %
)

###########################################################
## Working points for the 81X training (completed in 80X with variable fixes)
###########################################################
full_81x_chs_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id            
    Pt010_Tight    = cms.vdouble( 0.69, -0.35, -0.26, -0.21),
    Pt1020_Tight   = cms.vdouble( 0.69, -0.35, -0.26, -0.21),
    Pt2030_Tight   = cms.vdouble( 0.69, -0.35, -0.26, -0.21),
    Pt3050_Tight   = cms.vdouble( 0.86, -0.10, -0.05, -0.01),

    #Medium Id
    Pt010_Medium   = cms.vdouble( 0.18, -0.55, -0.42, -0.36),
    Pt1020_Medium  = cms.vdouble( 0.18, -0.55, -0.42, -0.36),
    Pt2030_Medium  = cms.vdouble( 0.18, -0.55, -0.42, -0.36),
    Pt3050_Medium  = cms.vdouble( 0.61, -0.35, -0.23, -0.17),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt1020_Loose   = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt2030_Loose   = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt3050_Loose   = cms.vdouble(-0.89, -0.52, -0.38, -0.30)
)

###########################################################
## Working points for the 80X training
###########################################################
full_80x_chs_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id            
    Pt010_Tight    = cms.vdouble( 0.26, -0.34, -0.24, -0.26),
    Pt1020_Tight   = cms.vdouble( 0.26, -0.34, -0.24, -0.26),
    Pt2030_Tight   = cms.vdouble( 0.26, -0.34, -0.24, -0.26),
    Pt3050_Tight   = cms.vdouble( 0.62, -0.21, -0.07, -0.03),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt1020_Medium  = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt2030_Medium  = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt3050_Medium  = cms.vdouble(-0.06, -0.42, -0.3 , -0.23),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt1020_Loose   = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt2030_Loose   = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt3050_Loose   = cms.vdouble(-0.92, -0.56, -0.44, -0.39)
)

###########################################################
## Working points for the 76X training
###########################################################
full_76x_chs_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0
    
    #Tight Id            
    Pt010_Tight    = cms.vdouble(0.09,-0.37,-0.24,-0.21),
    Pt1020_Tight   = cms.vdouble(0.09,-0.37,-0.24,-0.21),
    Pt2030_Tight   = cms.vdouble(0.09,-0.37,-0.24,-0.21),
    Pt3050_Tight   = cms.vdouble(0.52,-0.19,-0.06,-0.03),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.58,-0.52,-0.40,-0.36),
    Pt1020_Medium  = cms.vdouble(-0.58,-0.52,-0.40,-0.36),
    Pt2030_Medium  = cms.vdouble(-0.58,-0.52,-0.40,-0.36),
    Pt3050_Medium  = cms.vdouble(-0.20,-0.39,-0.24,-0.19),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.96,-0.62,-0.53,-0.49),
    Pt1020_Loose   = cms.vdouble(-0.96,-0.62,-0.53,-0.49),
    Pt2030_Loose   = cms.vdouble(-0.96,-0.62,-0.53,-0.49),
    Pt3050_Loose   = cms.vdouble(-0.93,-0.52,-0.39,-0.31)   
)

###########################################################
## Working points for the 74X training
###########################################################
full_74x_chs_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0
                
    #Tight Id                                                                                                                                                                                 
    Pt010_Tight    = cms.vdouble(-0.1,-0.83,-0.83,-0.98),
    Pt1020_Tight   = cms.vdouble(-0.1,-0.83,-0.83,-0.98),
    Pt2030_Tight   = cms.vdouble(-0.1,-0.83,-0.83,-0.98),
    Pt3050_Tight   = cms.vdouble(-0.5,-0.77,-0.80,-0.98),

    #Medium Id                                                                                                                                                                                  
    Pt010_Medium   = cms.vdouble(-0.3,-0.87,-0.87,-0.99),
    Pt1020_Medium  = cms.vdouble(-0.3,-0.87,-0.87,-0.99),
    Pt2030_Medium  = cms.vdouble(-0.3,-0.87,-0.87,-0.99),
    Pt3050_Medium  = cms.vdouble(-0.6,-0.85,-0.85,-0.99),

    #Loose Id                                                                                                                                                                                   
    Pt010_Loose    = cms.vdouble(-0.8,-0.97,-0.97,-0.99),
    Pt1020_Loose   = cms.vdouble(-0.8,-0.97,-0.97,-0.99),
    Pt2030_Loose   = cms.vdouble(-0.8,-0.97,-0.97,-0.99),
    Pt3050_Loose   = cms.vdouble(-0.8,-0.95,-0.97,-0.99)   
)

###########################################################
## Working points for the 53X training/New Met Dec 21, 2012
###########################################################
full_53x_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.83,-0.81,-0.74,-0.81),
    Pt1020_Tight   = cms.vdouble(-0.83,-0.81,-0.74,-0.81),
    Pt2030_Tight   = cms.vdouble( 0.73, 0.05,-0.26,-0.42),
    Pt3050_Tight   = cms.vdouble( 0.73, 0.05,-0.26,-0.42),
    
    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.83,-0.92,-0.90,-0.92),
    Pt1020_Medium  = cms.vdouble(-0.83,-0.92,-0.90,-0.92),
    Pt2030_Medium  = cms.vdouble( 0.10,-0.36,-0.54,-0.54),
    Pt3050_Medium  = cms.vdouble( 0.10,-0.36,-0.54,-0.54),
    
    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.95,-0.96,-0.94,-0.95),
    Pt1020_Loose   = cms.vdouble(-0.95,-0.96,-0.94,-0.95),
    Pt2030_Loose   = cms.vdouble(-0.63,-0.60,-0.55,-0.45),
    Pt3050_Loose   = cms.vdouble(-0.63,-0.60,-0.55,-0.45),
    
    #MET
    Pt010_MET	   = cms.vdouble( 0.  ,-0.6,-0.4,-0.4),
    Pt1020_MET     = cms.vdouble( 0.3 ,-0.2,-0.4,-0.4),
    Pt2030_MET     = cms.vdouble( 0.  , 0. , 0. , 0. ),
    Pt3050_MET     = cms.vdouble( 0.  , 0. ,-0.1,-0.2)
    )

full_53x_chs_wp  = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.83,-0.81,-0.74,-0.81),
    Pt1020_Tight   = cms.vdouble(-0.83,-0.81,-0.74,-0.81),
    Pt2030_Tight   = cms.vdouble( 0.78, 0.50, 0.17, 0.17),
    Pt3050_Tight   = cms.vdouble( 0.78, 0.50, 0.17, 0.17),
    
    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.83,-0.92,-0.90,-0.92),
    Pt1020_Medium  = cms.vdouble(-0.83,-0.92,-0.90,-0.92),
    Pt2030_Medium  = cms.vdouble(-0.07,-0.09, 0.00,-0.06),
    Pt3050_Medium  = cms.vdouble(-0.07,-0.09, 0.00,-0.06),
    
    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.95,-0.96,-0.94,-0.95),
    Pt1020_Loose   = cms.vdouble(-0.95,-0.96,-0.94,-0.95),
    Pt2030_Loose   = cms.vdouble(-0.15,-0.26,-0.16,-0.16),
    Pt3050_Loose   = cms.vdouble(-0.15,-0.26,-0.16,-0.16),
    )

met_53x_wp  = cms.PSet(
    
    #Tight Id
    Pt010_Tight    = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Tight   = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Tight   = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Tight   = cms.vdouble(-2, -2, -2, -2, -2),

                    #Medium Id
    Pt010_Medium   = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Medium  = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Medium  = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Medium  = cms.vdouble(-2, -2, -2, -2, -2),

                    #Loose Id
    Pt010_Loose    = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Loose   = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Loose   = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Loose   = cms.vdouble(-2, -2, -2, -2, -2),

    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0
    #MET
    Pt010_MET      = cms.vdouble(-0.2 ,-0.3,-0.5,-0.5),
    Pt1020_MET     = cms.vdouble(-0.2 ,-0.2,-0.5,-0.3),
    Pt2030_MET     = cms.vdouble(-0.2 ,-0.2,-0.2, 0.1),
    Pt3050_MET     = cms.vdouble(-0.2 ,-0.2, 0. , 0.2)
    )

metfull_53x_wp  = cms.PSet(
    #MET
    Pt010_MET      = cms.vdouble(-0.2 ,-0.3,-0.5,-0.5),
    Pt1020_MET     = cms.vdouble(-0.2 ,-0.2,-0.5,-0.3),
    Pt2030_MET     = cms.vdouble( 0.  , 0. , 0. , 0. ),
    Pt3050_MET     = cms.vdouble( 0.  , 0. ,-0.1,-0.2)
    )


###########################################################
## Working points for the 5X training
###########################################################
full_5x_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.47,-0.92,-0.92,-0.94),
    Pt1020_Tight   = cms.vdouble(-0.47,-0.92,-0.92,-0.94),
    Pt2030_Tight   = cms.vdouble(+0.32,-0.49,-0.61,-0.74),
    Pt3050_Tight   = cms.vdouble(+0.32,-0.49,-0.61,-0.74),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.83,-0.96,-0.95,-0.96),
    Pt1020_Medium  = cms.vdouble(-0.83,-0.96,-0.95,-0.96),
    Pt2030_Medium  = cms.vdouble(-0.40,-0.74,-0.76,-0.81),
    Pt3050_Medium  = cms.vdouble(-0.40,-0.74,-0.76,-0.81),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.95,-0.97,-0.97,-0.97),
    Pt1020_Loose   = cms.vdouble(-0.95,-0.97,-0.97,-0.97),
    Pt2030_Loose   = cms.vdouble(-0.80,-0.85,-0.84,-0.85),
    Pt3050_Loose   = cms.vdouble(-0.80,-0.85,-0.84,-0.85)
)

simple_5x_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0
    
    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.54,-0.93,-0.93,-0.94),
    Pt1020_Tight   = cms.vdouble(-0.54,-0.93,-0.93,-0.94),
    Pt2030_Tight   = cms.vdouble(+0.26,-0.54,-0.63,-0.74),
    Pt3050_Tight   = cms.vdouble(+0.26,-0.54,-0.63,-0.74),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.85,-0.96,-0.95,-0.96),
    Pt1020_Medium  = cms.vdouble(-0.85,-0.96,-0.95,-0.96),
    Pt2030_Medium  = cms.vdouble(-0.40,-0.73,-0.74,-0.80),
    Pt3050_Medium  = cms.vdouble(-0.40,-0.73,-0.74,-0.80),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.95,-0.97,-0.96,-0.97),
    Pt1020_Loose   = cms.vdouble(-0.95,-0.97,-0.96,-0.97),
    Pt2030_Loose   = cms.vdouble(-0.80,-0.86,-0.80,-0.84),
    Pt3050_Loose   = cms.vdouble(-0.80,-0.86,-0.80,-0.84)
    
)

###########################################################
## Working points for the 5X_CHS training
###########################################################
full_5x_chs_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.59,-0.75,-0.78,-0.80),
    Pt1020_Tight   = cms.vdouble(-0.59,-0.75,-0.78,-0.80),
    Pt2030_Tight   = cms.vdouble(+0.41,-0.10,-0.20,-0.45),
    Pt3050_Tight   = cms.vdouble(+0.41,-0.10,-0.20,-0.45),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.94,-0.91,-0.91,-0.92),
    Pt1020_Medium  = cms.vdouble(-0.94,-0.91,-0.91,-0.92),
    Pt2030_Medium  = cms.vdouble(-0.58,-0.65,-0.57,-0.67),
    Pt3050_Medium  = cms.vdouble(-0.58,-0.65,-0.57,-0.67),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.98,-0.95,-0.94,-0.94),
    Pt1020_Loose   = cms.vdouble(-0.98,-0.95,-0.94,-0.94),
    Pt2030_Loose   = cms.vdouble(-0.89,-0.77,-0.69,-0.75),
    Pt3050_Loose   = cms.vdouble(-0.89,-0.77,-0.69,-0.57)
)

simple_5x_chs_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.60,-0.74,-0.78,-0.81),
    Pt1020_Tight   = cms.vdouble(-0.60,-0.74,-0.78,-0.81),
    Pt2030_Tight   = cms.vdouble(-0.47,-0.06,-0.23,-0.47),
    Pt3050_Tight   = cms.vdouble(-0.47,-0.06,-0.23,-0.47),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.95,-0.94,-0.92,-0.91),
    Pt1020_Medium  = cms.vdouble(-0.95,-0.94,-0.92,-0.91),
    Pt2030_Medium  = cms.vdouble(-0.59,-0.65,-0.56,-0.68),
    Pt3050_Medium  = cms.vdouble(-0.59,-0.65,-0.56,-0.68),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.98,-0.96,-0.94,-0.94),
    Pt1020_Loose   = cms.vdouble(-0.98,-0.96,-0.94,-0.94),
    Pt2030_Loose   = cms.vdouble(-0.89,-0.75,-0.72,-0.75),
    Pt3050_Loose   = cms.vdouble(-0.89,-0.75,-0.72,-0.75)
)


###########################################################
## Working points for the 4X training
###########################################################
PuJetIdOptMVA_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.5,-0.2,-0.83,-0.7),
    Pt1020_Tight   = cms.vdouble(-0.5,-0.2,-0.83,-0.7),
    Pt2030_Tight   = cms.vdouble(-0.2,  0.,    0.,  0.),
    Pt3050_Tight   = cms.vdouble(-0.2,  0.,    0.,  0.),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.73,-0.89,-0.89,-0.83),
    Pt1020_Medium  = cms.vdouble(-0.73,-0.89,-0.89,-0.83),
    Pt2030_Medium  = cms.vdouble(0.1,  -0.4, -0.4, -0.45),
    Pt3050_Medium  = cms.vdouble(0.1,  -0.4, -0.4, -0.45),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.9,-0.9, -0.9,-0.9),
    Pt1020_Loose   = cms.vdouble(-0.9,-0.9, -0.9,-0.9),
    Pt2030_Loose   = cms.vdouble(-0.4,-0.85,-0.7,-0.6),
    Pt3050_Loose   = cms.vdouble(-0.4,-0.85,-0.7,-0.6)
)

PuJetIdMinMVA_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-0.5,-0.2,-0.83,-0.7),
    Pt1020_Tight   = cms.vdouble(-0.5,-0.2,-0.83,-0.7),
    Pt2030_Tight   = cms.vdouble(-0.2,  0.,    0.,  0.),
    Pt3050_Tight   = cms.vdouble(-0.2,  0.,    0.,  0.),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-0.73,-0.89,-0.89,-0.83),
    Pt1020_Medium  = cms.vdouble(-0.73,-0.89,-0.89,-0.83),
    Pt2030_Medium  = cms.vdouble(0.1,  -0.4, -0.5, -0.45),
    Pt3050_Medium  = cms.vdouble(0.1,  -0.4, -0.5, -0.45),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-0.9,-0.9, -0.94,-0.9),
    Pt1020_Loose   = cms.vdouble(-0.9,-0.9, -0.94,-0.9),
    Pt2030_Loose   = cms.vdouble(-0.4,-0.85,-0.7,-0.6),
    Pt3050_Loose   = cms.vdouble(-0.4,-0.85,-0.7,-0.6)
)

EmptyJetIdParams = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt1020_Tight   = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt2030_Tight   = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt3050_Tight   = cms.vdouble(-999.,-999.,-999.,-999.),

    #Medium Id
    Pt010_Medium   = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt1020_Medium  = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt2030_Medium  = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt3050_Medium  = cms.vdouble(-999.,-999.,-999.,-999.),

    #Loose Id
    Pt010_Loose    = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt1020_Loose   = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt2030_Loose   = cms.vdouble(-999.,-999.,-999.,-999.),
    Pt3050_Loose   = cms.vdouble(-999.,-999.,-999.,-999.)
)


PuJetIdCutBased_wp = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0
    #betaStarClassic/log(nvtx-0.64) Values
    #Tight Id
    Pt010_BetaStarTight    = cms.vdouble( 0.15, 0.15, 999., 999.),
    Pt1020_BetaStarTight   = cms.vdouble( 0.15, 0.15, 999., 999.),
    Pt2030_BetaStarTight   = cms.vdouble( 0.15, 0.15, 999., 999.),
    Pt3050_BetaStarTight   = cms.vdouble( 0.15, 0.15, 999., 999.),
    
    #Medium Id => Daniele
    Pt010_BetaStarMedium   = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt1020_BetaStarMedium  = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt2030_BetaStarMedium  = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt3050_BetaStarMedium  = cms.vdouble( 0.2, 0.3, 999., 999.),
    
    #Loose Id
    Pt010_BetaStarLoose    = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt1020_BetaStarLoose   = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt2030_BetaStarLoose   = cms.vdouble( 0.2, 0.3, 999., 999.),
    Pt3050_BetaStarLoose   = cms.vdouble( 0.2, 0.3, 999., 999.),

    #RMS variable
    #Tight Id
    Pt010_RMSTight         = cms.vdouble( 0.06, 0.07, 0.04, 0.05),
    Pt1020_RMSTight        = cms.vdouble( 0.06, 0.07, 0.04, 0.05),
    Pt2030_RMSTight        = cms.vdouble( 0.05, 0.07, 0.03, 0.045),
    Pt3050_RMSTight        = cms.vdouble( 0.05, 0.06, 0.03, 0.04),
    
    #Medium Id => Daniele
    Pt010_RMSMedium        = cms.vdouble( 0.06, 0.03, 0.03, 0.04),
    Pt1020_RMSMedium       = cms.vdouble( 0.06, 0.03, 0.03, 0.04),
    Pt2030_RMSMedium       = cms.vdouble( 0.06, 0.03, 0.03, 0.04),
    Pt3050_RMSMedium       = cms.vdouble( 0.06, 0.03, 0.03, 0.04),
    
    #Loose Id
    Pt010_RMSLoose         = cms.vdouble( 0.06, 0.05, 0.05, 0.07),
    Pt1020_RMSLoose        = cms.vdouble( 0.06, 0.05, 0.05, 0.07),
    Pt2030_RMSLoose        = cms.vdouble( 0.06, 0.05, 0.05, 0.055),
    Pt3050_RMSLoose        = cms.vdouble( 0.06, 0.05, 0.05, 0.055)
    )


JetIdParams = cms.PSet(
    #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

    #Tight Id
    Pt010_Tight    = cms.vdouble( 0.5,0.6,0.6,0.9),
    Pt1020_Tight   = cms.vdouble(-0.2,0.2,0.2,0.6),
    Pt2030_Tight   = cms.vdouble( 0.3,0.4,0.7,0.8),
    Pt3050_Tight   = cms.vdouble( 0.5,0.4,0.8,0.9),

    #Medium Id
    Pt010_Medium   = cms.vdouble( 0.2,0.4,0.2,0.6),
    Pt1020_Medium  = cms.vdouble(-0.3,0. ,0. ,0.5),
    Pt2030_Medium  = cms.vdouble( 0.2,0.2,0.5,0.7),
    Pt3050_Medium  = cms.vdouble( 0.3,0.2,0.7,0.8),

    #Loose Id
    Pt010_Loose    = cms.vdouble( 0. , 0. , 0. ,0.2),
    Pt1020_Loose   = cms.vdouble(-0.4,-0.4,-0.4,0.4),
    Pt2030_Loose   = cms.vdouble( 0. , 0. , 0.2,0.6),
    Pt3050_Loose   = cms.vdouble( 0. , 0. , 0.6,0.2)
)

