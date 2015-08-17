#include <vector>

namespace HGCalTriggerBackend{
    //  this class is design to contain and compute 
    //  efficiently the cluster shapes
    //  running only once on the cluster members.
    class ClusterShapes{
    private: 
        float sum_e = 0.0;
        float sum_logE = 0.0;
        int n=1;

        float emax = 0.0;

        float sum_w =0.0; // just here for clarity
        float sum_eta = 0.0;
        float sum_r  = 0.0;
        // i will discriminate using the rms in -pi,pi or in 0,pi
        float sum_phi_0 = 0.0; // computed in -pi,pi
        float sum_phi_1 = 0.0; // computed in 0, 2pi

        float sum_eta2=0.0;
        float sum_r2 = 0.0;
        float sum_phi2_0=0.0; //computed in -pi,pi
        float sum_phi2_1=0.0; //computed in 0,2pi

        // off diagonal element of the tensor
        float sum_eta_r =0.0;
        float sum_r_phi_0 = 0.0;
        float sum_r_phi_1 = 0.0;
        float sum_eta_phi_0 = 0.0;
        float sum_eta_phi_1 = 0.0;

        bool isPhi0 = true;
    public:

        // --- this is what I need to set
        float e; // -> e, logE
        float phi;
        float r;
        float eta;
        void SetClusterShapes();
        

        // --- this is what I want out:
        float SigmaEtaEta();
        float SigmaPhiPhi();
        float SigmaRR();
        // ----
        float Phi();
        float R();
        float Eta();
        inline int N(){return n;}
        // --
        float SigmaEtaR();
        float SigmaEtaPhi();
        float SigmaRPhi();

        ClusterShapes operator+(const ClusterShapes &);
        void operator+=(const ClusterShapes &);
    };

}; // end namespace



// -----------------------------------
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
