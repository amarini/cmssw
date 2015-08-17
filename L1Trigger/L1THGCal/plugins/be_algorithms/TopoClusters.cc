#include "L1Trigger/L1THGCal/interface/HGCalTriggerBackendAlgorithmBase.h"
#include "L1Trigger/L1THGCal/interface/fe_codecs/HGCal64BitRandomCodec.h"

#include "DataFormats/L1THGCal/interface/HGCalCluster.h"


using namespace HGCalTriggerBackend;
using namespace std;

#include "L1Trigger/L1THGCal/interface/UnionFind.h"


template<typename CODEC>
class TopoClustersAlgo : public Algorithm<CODEC>
{
    private:
        std::auto_ptr<l1t::HGCalClusterBxCollection> cluster_product;
        uint32_t threshold_;
    public:
        // --- constructor
        TopoClustersAlgo(const edm::ParameterSet& conf) :
            Algorithm<CODEC>(conf){}
        // --- destructor
        ~TopoClustersAlgo() {}
        // --- Inherited 
        virtual void setProduces(edm::EDProducer& prod) const override final 
        {
            prod.produces<l1t::HGCalClusterBxCollection>(this->name());
        }

        virtual void run(const l1t::HGCFETriggerDigiCollection& coll,
                const std::unique_ptr<HGCalTriggerGeometryBase>& geom) override final;

        virtual void putInEvent(edm::Event& evt) override final 
        {
            evt.put(cluster_product,this->name());
        }

        virtual void reset() override final {
            cluster_product.reset( new l1t::HGCalClusterBxCollection );
        }

};

// -------------- END OF HEADERS -----------

// --- actual algorithm --
template<typename CODEC>
void TopoClustersAlgo<CODEC>::run( const l1t::HGCFETriggerDigiCollection & coll, const std::unique_ptr<HGCalTriggerGeometryBase> &geom)
{
    UFCluster<uint32_t,uint32_t> processedClusters;
    // -- locate the seeds or local maxima 
    for(const auto& digi : coll)
    {
        HGCal64BitRandomCodec::data_type my_data;  
        uint32_t id = digi.id();
        const std::unique_ptr<const HGCalTriggerGeometry::Module>      m = geom -> getModuleFromCell(id);
        const std::unique_ptr<const HGCalTriggerGeometry::TriggerCell> c = geom -> getTriggerCellFromCell(id);
      
        //if ( processedClusters.search(id)  ) continue; // already processed, can't be ?

        digi.decode(this->codec_,my_data);
        uint32_t rawenergy = 100; // ?  decode ? , energy 

        if (rawenergy < this->threshold ) continue; 

        processedClusters.add(id, rawenergy ); 
        // check neighbours
        for( const auto& n : c -> neighbours() )
        {
            //uint32_t nid = n . triggerCellId()   ;
            uint32_t nid = n;
            if (not processedClusters.search(nid)  ) continue;  // not processed yet
            processedClusters.Union( id, nid ) ; // if both in the clusters and they are neighbours merge them
        }

    }

}

// --------------- PLUGIN DEFINITION -----------
// DEFINE_EDM_PLUGIN(HGCalTriggerBackendAlgorithmFactory, 
//         TopoClustersAlgo,
//         "TopoClustersAlgo");
// -----------------------------------
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
