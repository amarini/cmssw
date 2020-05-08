
/**
 * This is a Herwig++-specific parton selector that selects all status==2 partons. This is likely a temporary choice since
 * Herwig++ status codes in CMSSW currently break the HepMC convention. Once the status codes are fixed, the selector will
 * be updated.
 */

#include "PhysicsTools/JetMCAlgos/interface/HerwigppPartonSelector.h"
#include "PhysicsTools/JetMCUtils/interface/CandMCTag.h"

HerwigppPartonSelector::HerwigppPartonSelector() {}

HerwigppPartonSelector::~HerwigppPartonSelector() {}

void HerwigppPartonSelector::run(const edm::Handle<reco::GenParticleCollection>& particles,
                                 std::unique_ptr<reco::GenParticleRefVector>& partons) {
  // loop over particles and select partons
  for (reco::GenParticleCollection::const_iterator it = particles->begin(); it != particles->end(); ++it) {
    if (it->status() != 2 and not (it->status() >=11 and it->status()<=200) )
      continue;  // only accept status 2 and between 11--200 (see below for documentation)
    if (!CandMCTagUtils::isParton(*it))
      continue;  // skip particle if not a parton

    partons->push_back(reco::GenParticleRef(particles, it - particles->begin()));
  }

  return;
}

/* From the H7 documentation page: https://herwig.hepforge.org/tutorials/faq/general.html
Since Herwig++ 2.4.0, we assign status codes according to this scheme:

        0 : an empty entry, with no meaningful information and therefore to be skipped unconditionally
        1 : a final-state particle, i.e. a particle that is not decayed further by the generator (may also include unstable particles that are to be decayed later, as part of the detector simulation). Such particles must always be labelled '1'.
        2 : a decayed Standard Model hadron or tau or mu lepton, excepting virtual intermediate states thereof (i.e. the particle must undergo a normal decay, not e.g. a shower branching). Such particles must always be labelled '2'. No other particles can be labelled '2'.
        3 : a documentation entry
        4 : an incoming beam particle
        11 - 200 : an intermediate (decayed/branched/...) particle that does not fulfill the criteria of status code 2, with a generator-dependent classification of its nature
*/ 
