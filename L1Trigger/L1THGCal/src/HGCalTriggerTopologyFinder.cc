#include "L1Trigger/L1THGCal/interface/HGCalTriggerTopologyFinder.h"

using namespace HGCalTriggerGeometry;

int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTriggerCells(HGCalTriggerGeometryBase & mTriggerGeometry) 
{
   edm::LogInfo("HGCalTriggerTopologyFinder::initTriggerCells")<<
	   "Initialiazing trigger cell topology from hgcal topology";

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
		        std::stringstream compstream("");
		 	for(auto & cell : tcell.second -> components()  ) 
			{
				compstream << cell<<": " ; // I need to reapet because I want the neigh per HGCal Cell for debug
				for(auto & nb_id :  mTopology . north( cell) )
					compstream <<"N "<< unsigned(nb_id )<<"|";
				for(auto & nb_id :  mTopology . south( cell)  )
					compstream <<"S " << unsigned(nb_id) <<"|";
				for(auto & nb_id :  mTopology . east( cell) )
					compstream <<"E " << unsigned(nb_id) <<"|";
				for(auto & nb_id :  mTopology . west( cell) )
					compstream <<"W " << unsigned(nb_id) <<"|";
				for(auto & nb_id :  mTopology . up( cell) )
					compstream <<"U " << unsigned(nb_id) <<"|";
				for(auto & nb_id :  mTopology . down( cell) )
					compstream <<"D " << unsigned(nb_id) <<"|";
				compstream <<"\n";
			}

	   		throw cms::Exception("HGCalTriggerTopologyFinder::initTriggerCells")
				<<"HGCal Cell ID="<<n.first <<" referenced in trigger cell (id="<< tcell.first<<")  components:"
				<< compstream.str() 
				<<", but not present in the map";
	    }


            unsigned neigh_tc =  triggercell -> triggerCellId();
            //- remove the cells that are in the trigger cell
            if (neigh_tc == tcell.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
            //tcell . second  -> neighbours_ . insert (  neigh_tc ) ; // use n.second if you want directions
	    insertNeighbour( tcell.second.get(), neigh_tc, n.second);
        }
    } // tcell loop

   edm::LogInfo("HGCalTriggerTopologyFinder::initTriggerCells")<<"Done";
   return 0;
}

// ----
int HGCalTriggerGeometry::HGCalTriggerTopologyFinder::initTriggerModules(HGCalTriggerGeometryBase & mTriggerGeometry) 
{

    // I need access to the non-const objects
   edm::LogInfo("HGCalTriggerTopologyFinder::initTriggerModules")<<"init module topology from trigger cell topology";

    // loop over modules
    for( auto & tmod : get_modules_inconstruction(mTriggerGeometry) ) //  map : unsigned ->  Module
    {
        std::map< unsigned, HGCalTriggerGeometry::TopoBits >  neigh;

        for(const unsigned & tcell_id : tmod.second -> components()  )
        {
            // I used these methods, so if we want to collect also this informations is simplier
	    //                                                                  [ id ] remove const 
            for (const auto & tcell_n : mTriggerGeometry . triggerCells() . find( tcell_id ) -> second -> neighbours()  ) // neihbours tr cells are filled
                neigh[ tcell_n.first ] |=  tcell_n.second; 
	    	// auto is a topo_list_type
                //neigh[ tcell_n ] |=  HGCalTriggerGeometry::generic; // TODO -- north sud ovest west

        } // components loop
        // ---
        for (auto & n : neigh ) 
        {
            //- find the tr cells that corresponds to the neigh cells
	    Module *module = getModuleFromCellInConstruction(mTriggerGeometry, n.first );
	    if ( module == NULL) {
		        std::stringstream compstream("");
		 	for(auto & mod : tmod.second -> components()  ) compstream << mod<<" " ;

	    		throw cms::Exception("HGCalTriggerTopologyFinder::initTriggerModule")
				<<"Trigger Cell ID="<<n.first
				<<" referenced in trigger module ("<<tmod.first<<") components:"
				<< compstream.str()
				<<", but not present in the map";
	    }
            unsigned neigh_mod =  module -> moduleId();
            //- remove the cells that are in the trigger cell
            if (neigh_mod == tmod.first) continue; // I am what I am and what I am needs no excuses
            //- add them to the list of neighbours
            //tmod . second  -> neighbours_ . insert (  neigh_mod ) ; // use n.second if you want directions TODO
	    insertNeighbour( tmod . second.get(), neigh_mod, n.second );
        }
    } // tcell loop

   edm::LogInfo("HGCalTriggerTopologyFinder::initTriggerModules")<<"Done";
    return 0;
}

HGCalTriggerGeometry::HGCalTriggerGeometryModifier* HGCalTriggerGeometryModifierFactory::create(const std::string &name,  const HGCalGeometry &g) {
                const auto& i = table_.find(name);
                if ( i == table_.end() ) {
			throw cms::Exception("HGCalTriggerGeometryModifierFactory::create")<< 
				"Unable to construct class named "<<name;
			return (HGCalTriggerGeometryModifier*)NULL;
		}
                else return i -> second ->create(g);
                };

REGISTER(HGCalTriggerGeometry::HGCalTriggerTopologyFinder);
