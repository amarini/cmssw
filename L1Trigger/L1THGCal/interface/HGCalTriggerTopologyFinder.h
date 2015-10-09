#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "L1Trigger/L1THGCal/interface/HGCalTriggerGeometryBase.h"
#include "DataFormats/ForwardDetId/interface/HGCTriggerDetId.h"

#include "Geometry/FCalGeometry/interface/HGCalGeometry.h"
#include "Geometry/CaloTopology/interface/CaloTopology.h"

#include <vector>
#include <iostream>
#include <fstream>
#include <map>

/* Original Author: Andrea Carlo Marini
 * email : andrea.carlo.marini@cern.ch
 * date : 09/10/2015
 *
 * This plugins want to read the HGCal geometry/topology and fill the Trigger geometry with a navigation system.
 * May be slow, but generic
 */

#ifndef HGCAL_TRIGGERTOPOLOGY_FINDER_H
#define HGCAL_TRIGGERTOPOLOGY_FINDER_H 1

namespace HGCalTriggerGeometry{

    typedef uint8_t TopoBits;

    enum TopoBit{
         north   = 1UL <<0 ,
         south   = 1UL <<1,
         east    = 1UL <<2,
         west    = 1UL <<3,
         up      = 1UL <<4,
         down    = 1UL <<5,
         generic = 1UL <<6 // if nswe is not known, not guarrantee to be set if something else is
    };


class HGCalTriggerTopologyFinder{	
   // const HGCalTopology & mTopology; geometry knows about topology
    const HGCalGeometry & mGeometry;

    // fill tr cell neigh
    int initTC(HGCalTriggerGeometryBase &);
    //fill tr module neigh
    int initTM(HGCalTriggerGeometryBase &);


public:

    HGCalTriggerTopologyFinder( const HGCalGeometry &g): mGeometry(g) {} 
   
    // this is const 
    inline int initialize(HGCalTriggerGeometryBase &g ) 
    { return initTC(g) | initTM(g) ; }
        
};

}; // namespace


#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 
