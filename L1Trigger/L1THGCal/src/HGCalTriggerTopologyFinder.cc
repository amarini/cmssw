#include "L1Trigger/L1THGCal/interface/HGCalTriggerTopologyFinder.h"

using namespace HGCalTriggerGeometry;

int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTC(HGCalTriggerGeometryBase & mTriggerGeometry) 
{

    const HGCalTopology& mTopology =  mGeometry.topology () ;
    // I need access to the non-const objects

    // loop over cells
    for( auto & tcell : mTriggerGeometry.trigger_cells_ ) // trigger cells map : unsigned -> triggerCell
    {
        std::map< unsigned, HGCalTriggerGeometry::TopoBits >  neigh;

        for(auto & cell : tcell.second -> components()  )
        {
            // I used these methods, so if we want to collect also this informations is simplier
            for (auto id : mTopology . north( cell )  )
                neigh[id] |=  HGCalTriggerGeometry::north;
            for (auto id : mTopology . south( cell  ) )
                neigh[id] |=  HGCalTriggerGeometry::south;
            for (auto id : mTopology . east(  cell  ) )
                neigh[id] |=  HGCalTriggerGeometry::east;
            for (auto id : mTopology . west( cell  ) )
                neigh[id] |=  HGCalTriggerGeometry::west;
            for (auto id : mTopology . up(    cell  ) )
                neigh[id] |=  HGCalTriggerGeometry::up;
            for (auto id : mTopology . down(  cell  ) )
                neigh[id] |=  HGCalTriggerGeometry::down;

        } // components loop
        // ---
        for (auto & n : neigh ) 
        {
            //- find the tr cells that corresponds to the neigh cells
            unsigned neigh_tc =  mTriggerGeometry . getTriggerCellFromCell( n.first ) -> triggerCellId();
            //- remove the cells that are in the trigger cell
            if (neigh_tc == tcell.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
	    //I need to cast away constantness :(
            const_cast<HGCalTriggerGeometry::TriggerCell*> (tcell . second .get()) -> neighbours_ . insert (  neigh_tc ) ; // use n.second if you want directions TODO
        }
    } // tcell loop

    return 0;
}

// ----
int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTM(HGCalTriggerGeometryBase & mTriggerGeometry) 
{

    // I need access to the non-const objects

    // loop over modules
    for( auto & tmod : mTriggerGeometry.modules_ ) //  map : unsigned ->  Module
    {
        std::map< unsigned, HGCalTriggerGeometry::TopoBits >  neigh;

        for(const unsigned & tcell_id : tmod.second -> components()  )
        {
            // I used these methods, so if we want to collect also this informations is simplier
	    //                                                                  [ id ] remove const 
            for (const unsigned & tcell_n : mTriggerGeometry . triggerCells() . find( tcell_id ) -> second -> neighbours()  ) // neihbours tr cells are filled
                neigh[ tcell_n ] |=  HGCalTriggerGeometry::generic; // TODO -- north sud ovest west

        } // components loop
        // ---
        for (auto & n : neigh ) 
        {
            //- find the tr cells that corresponds to the neigh cells
            unsigned neigh_mod =  mTriggerGeometry . getModuleFromTriggerCell( n.first ) -> moduleId();
            //- remove the cells that are in the trigger cell
            if (neigh_mod == tmod.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
	    //I need to cast away constantness :(
            const_cast<HGCalTriggerGeometry::Module*> (tmod . second .get()) -> neighbours_ . insert (  neigh_mod ) ; // use n.second if you want directions TODO
        }
    } // tcell loop

    return 0;
}
