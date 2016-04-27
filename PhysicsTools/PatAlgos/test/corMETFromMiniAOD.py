import FWCore.ParameterSet.Config as cms

# Define the CMSSW process
process = cms.Process("RERUN")

# Load the standard set of configuration modules
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# Message Logger settings
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Set the process options -- Display summary at the end, enable unscheduled execution
process.options = cms.untracked.PSet( 
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False) 
)

# How many events to process
process.maxEvents = cms.untracked.PSet( 
   input = cms.untracked.int32(100)
)

#configurable options =======================================================================
runOnData=False #data/MC switch
usePrivateSQlite=False #use external JECs (sqlite file)
useHFCandidates=True #create an additionnal NoHF slimmed MET collection if the option is set to false
redoPuppi=False # rebuild puppiMET
#===================================================================


### External JECs =====================================================================================================

#from Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff import *
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
from Configuration.AlCa.autoCond import autoCond
##___________________________External JECs________________________________||
if runOnData:
 process.GlobalTag.globaltag = '76X_dataRun2_16Dec2015_v0'
else:
 process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'

## Private SQlite files to be taken from
## https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC#Recommended_for_Data
## https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC#Recommended_for_MC
if usePrivateSQlite:
    from CondCore.DBCommon.CondDBSetup_cfi import *
    import os
    if runOnData:
      era="Summer15_50nsV5_DATA"
    else:
      era="Summer15_50nsV5_MC"
      
    process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                               connect = cms.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS"),
                               toGet =  cms.VPSet(
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PF"),
          label= cms.untracked.string("AK4PF")
          ),
        cms.PSet(
          record = cms.string("JetCorrectionsRecord"),
          tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PFchs"),
          label= cms.untracked.string("AK4PFchs")
          ),
        )
                               )
    process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')

### =====================================================================================================
#process.load("JetMETCorrections.Modules.JetResolutionESProducer_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *

##___________________________External JER file________________________________||
##https://github.com/cms-jet/JRDatabase/tree/master/SQLiteFiles
process.jer = cms.ESSource("PoolDBESSource",CondDBSetup,
                           #connect = cms.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS"),
                           #connect = cms.string( "frontier://FrontierPrep/CMS_CONDITIONS"),
                           connect = cms.string("sqlite:PhysicsTools/PatUtils/data/Fall15_25nsV2_MC.db"),
                           toGet =  cms.VPSet(
    cms.PSet(
      record = cms.string('JetResolutionRcd'),
      #tag    = cms.string('JR_MC_PtResolution_Summer15_25nsV6_AK4PF'),
      tag    = cms.string('JR_Fall15_25nsV2_MC_PtResolution_AK4PFchs'),
      label  = cms.untracked.string('AK4PFchs_pt')
      ),
    cms.PSet(
      record = cms.string("JetResolutionRcd"),
      #tag = cms.string("JR_MC_PhiResolution_Summer15_25nsV6_AK4PF"),
      tag = cms.string("JR_Fall15_25nsV2_MC_PhiResolution_AK4PFchs"),
      label= cms.untracked.string("AK4PFchs_phi")
      ),
    cms.PSet(
      record = cms.string('JetResolutionScaleFactorRcd'),
      #tag    = cms.string('JR_DATAMCSF_Summer15_25nsV6_AK4PFchs'),
      tag    = cms.string('JR_Fall15_25nsV2_MC_SF_AK4PFchs'),
      label  = cms.untracked.string('AK4PFchs')
      ),
    
    ) )
process.es_prefer_jer = cms.ESPrefer("PoolDBESSource",'jer')


# Define the input source
if runOnData:
  #75X file : root://eoscms//eos/cms/store/relval/CMSSW_7_5_0/SingleElectron/MINIAOD/75X_dataRun1_HLT_v1_RelVal_electron2012D-v1/00000/A4BD1262-8F2B-E511-8470-002618943964.root
  #74X file : root://eoscms.cern.ch//store/data/Run2015B/JetHT/MINIAOD/PromptReco-v1/000/251/252/00000/263D331F-AF27-E511-969B-02163E012627.root
  fname = 'root://eoscms.cern.ch//store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v4/000/260/607/00000/36558DE4-1484-E511-AA5C-02163E01442E.root'
else:
  #75X file : root://eoscms.cern.ch//store/relval/CMSSW_7_5_0/RelValTTbar_13/MINIAODSIM/75X_mcRun2_asymptotic_v1-v1/00000/92A928E7-842A-E511-87CC-0025905A60E0.root
  #74X file : root://eoscms.cern.ch//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v2/60000/001C7571-0511-E511-9B8E-549F35AE4FAF.root
#  fname = 'root://eoscms.cern.ch//store/relval/CMSSW_7_5_3/RelValZEE_13/MINIAODSIM/75X_mcRun2_asymptotic_v5-v1/00000/F8C5D3F4-A861-E511-BA41-002618943906.root'
  fname = 'root://eoscms.cern.ch//store/relval/CMSSW_7_6_4/RelValZMM_13/MINIAODSIM/76X_mcRun2_asymptotic_v14_reHLTref-v1/00000/28DBC5FA-D7EF-E511-AE1E-0CC47A78A426.root'
  
# Define the input source
process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring([ fname ])
)


### ---------------------------------------------------------------------------
### Removing the HF from the MET computation
### ---------------------------------------------------------------------------
if not useHFCandidates:
    process.noHFCands = cms.EDFilter("CandPtrSelector",
                                     src=cms.InputTag("packedPFCandidates"),
                                     cut=cms.string("abs(pdgId)!=1 && abs(pdgId)!=2 && abs(eta)<3.0")
                                     )

#jets are rebuilt from those candidates by the tools, no need to do anything else
### =================================================================================

from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

#default configuration for miniAOD reprocessing, change the isData flag to run on data
#for a full met computation, remove the pfCandColl input
runMetCorAndUncFromMiniAOD(process,
                           isData=runOnData,
                           )

if not useHFCandidates:
    runMetCorAndUncFromMiniAOD(process,
                               isData=runOnData,
                               pfCandColl=cms.InputTag("noHFCands"),
                               reclusterJets=True, #needed for NoHF
                               recoMetFromPFCs=True, #needed for NoHF
                               postfix="NoHF"
                               )

if redoPuppi:
  from PhysicsTools.PatAlgos.slimming.puppiForMET_cff import makePuppiesFromMiniAOD
  makePuppiesFromMiniAOD( process );

  runMetCorAndUncFromMiniAOD(process,
                             isData=runOnData,
                             pfCandColl=cms.InputTag("puppiForMET"),
                             recoMetFromPFCs=True,
                             reclusterJets=True,
                             jetFlavor="AK4PFPuppi",
                             postfix="Puppi"
                             )

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring( "keep *_slimmedMETs_*_*",
                                            "keep *_slimmedMETsNoHF_*_*",
                                            "keep *_slimmedMETsPuppi_*_*",
                                            ),
    fileName = cms.untracked.string('corMETMiniAOD.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    fastCloning = cms.untracked.bool(False),
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)


process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)
