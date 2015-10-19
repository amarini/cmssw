#include "L1Trigger/L1THGCal/interface/HGCalTriggerTopologyFinder.h"

using namespace HGCalTriggerGeometry;

int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTriggerCells(HGCalTriggerGeometryBase & mTriggerGeometry) 
{

    const HGCalTopology& mTopology =  mGeometry.topology () ;
    // I need access to the non-const objects

    // loop over cells
    for( auto & tcell : get_triggercells_inconstruction(mTriggerGeometry)) // trigger cells map : unsigned -> triggerCell
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
            //unsigned neigh_tc =  mTriggerGeometry . getTriggerCellFromCellInConstruction( n.first ) -> triggerCellId();
	    //
	    TriggerCell *triggercell = getTriggerCellFromCellInConstruction(mTriggerGeometry, n.first ) ;
	    if (triggercell == NULL) {
	   		cms::Exception("HGCalTriggerTopologyFinder::initTriggerCells")<<
				"Trigger Cell referenced but not present in the map";
	    }
            unsigned neigh_tc =  triggercell -> triggerCellId();
            //- remove the cells that are in the trigger cell
            if (neigh_tc == tcell.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
            //tcell . second  -> neighbours_ . insert (  neigh_tc ) ; // use n.second if you want directions TODO
	    insertNeighbour( tcell.second.get(), neigh_tc);
        }
    } // tcell loop

    return 0;
}

// ----
int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTriggerModules(HGCalTriggerGeometryBase & mTriggerGeometry) 
{

    // I need access to the non-const objects

    // loop over modules
    for( auto & tmod : get_modules_inconstruction(mTriggerGeometry) ) //  map : unsigned ->  Module
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
	    Module *module = getModuleFromCellInConstruction(mTriggerGeometry, n.first );
	    if ( module == NULL) {
	    	cms::Exception("HGCalTriggerTopologyFinder::initTriggerModule")<<
			"Trigger Module referenced but not present in the map";
	    }
            unsigned neigh_mod =  module -> moduleId();
            //- remove the cells that are in the trigger cell
            if (neigh_mod == tmod.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
            //tmod . second  -> neighbours_ . insert (  neigh_mod ) ; // use n.second if you want directions TODO
	    insertNeighbour( tmod . second.get(), neigh_mod );
        }
    } // tcell loop

    return 0;
}
