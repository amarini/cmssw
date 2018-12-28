import FWCore.ParameterSet.Config as cms
process = cms.Process("runRivetAnalysis")

process.options   = cms.untracked.PSet(                           
    allowUnscheduled = cms.untracked.bool(False)
) 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.source = cms.Source("PoolSource",  fileNames = cms.untracked.vstring(
    # test on 94X
    #'/store/mc/RunIIFall17MiniAODv2/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/110000/FC2C0193-10BB-E811-9C06-FA163E23B3D2.root',
    '/store/mc/RunIIFall17MiniAODv2/VBFHToZG_ZToLL_M-125_13TeV_powheg_pythia8_TuneCP5Up/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/4604D45E-CDB6-E811-A279-FA163E575C2E.root',
    # just run a lot of MINIAOD

),
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.rivetProducerHTXS = cms.EDProducer('HTXSRivetProducer',
  HepMCCollection = cms.InputTag('myGenerator','unsmeared'),
  LHERunInfo = cms.InputTag('externalLHEProducer'),
  #ProductionMode = cms.string('GGF'),
  #ProductionMode = cms.string('WH'),
  ProductionMode = cms.string('AUTO'),
)

#MINIAOD
process.mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
    inputPruned = cms.InputTag("prunedGenParticles"),
    inputPacked = cms.InputTag("packedGenParticles"),
)
process.myGenerator = cms.EDProducer("GenParticles2HepMCConverter",
    genParticles = cms.InputTag("mergedGenParticles"),
    genEventInfo = cms.InputTag("generator"),
    signalParticlePdgIds = cms.vint32(25), ## for the Higgs analysis
)
process.p = cms.Path(process.mergedGenParticles*process.myGenerator*process.rivetProducerHTXS)

# # AOD
#process.myGenerator = cms.EDProducer("GenParticles2HepMCConverterHTXS",
#    genParticles = cms.InputTag("genParticles"),
#    genEventInfo = cms.InputTag("generator"),
#)
#process.p = cms.Path(process.myGenerator*process.rivetProducerHTXS)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *','keep *_*_*_runRivetAnalysis','keep *_generator_*_*','keep *_externalLHEProducer_*_*'),
    fileName = cms.untracked.string('testHTXSRivet_ggH4l_MINIAOD_100k.root')
)
process.o = cms.EndPath( process.out )
