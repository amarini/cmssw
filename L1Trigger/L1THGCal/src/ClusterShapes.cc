#include "L1Trigger/L1THGCal/interface/ClusterShapes.h"

using namespace HGCalTriggerBackend;

ClusterShapes ClusterShapes::operator+(const ClusterShapes& x)
{
    ClusterShapes cs(*this); // copy constructor
    cs += x;
    return cs;
}


void ClusterShapes::operator +=(const ClusterShapes &x){

	sum_e += x.sum_e;
	sum_logE += x.sum_logE;
	n += x.n;

    sum_w += x.sum_w;

    emax = (emax> x.emax) ? emax: x.emax;

    // mid-point
    sum_eta += x.sum_eta;
    sum_phi_0 += x.sum_phi_0; //
    sum_phi_1 += x.sum_phi_1; //
    sum_r   += x.sum_r;

    // square
    sum_eta2 += x.sum_eta2;
    sum_phi2_0 += x.sum_phi2_0;
    sum_phi2_1 += x.sum_phi2_1;
    sum_r2 += x.sum_r2;

    // off diagonal
    sum_eta_r     += x.sum_eta_r    ;
    sum_r_phi_0   += x.sum_r_phi_0  ;
    sum_r_phi_1   += x.sum_r_phi_1  ;
    sum_eta_phi_0 += x.sum_eta_phi_0;
    sum_eta_phi_1 += x.sum_eta_phi_1;

}

#include "TMath.h"

#include <cmath>

// -------------- CLUSTER SHAPES ---------------
void ClusterShapes::SetClusterShapes(){
    sum_e = e;
    sum_logE = TMath::Log(e);

    float w = e;

    
    sum_w = w;

    sum_phi_0 = w *( phi );
    sum_phi_1 = w* (phi + M_PI);
    sum_r = w * r;
    sum_eta = w * eta;

    //--
    sum_r2     += w * (r*r);
    sum_eta2   += w * (eta*eta);
    sum_phi2_0 += w * (phi*phi);
    sum_phi2_1 += w * (phi+M_PI)*(phi+M_PI);

    // -- off diagonal
    sum_eta_r += w * (r*eta);
    sum_r_phi_0 += w* (r *phi);
    sum_r_phi_1 += w* r *(phi + M_PI);
    sum_eta_phi_0 += w* (eta *phi);
    sum_eta_phi_1 += w* eta * (phi+M_PI);

}
// ------
float ClusterShapes::Eta(){eta =sum_eta/sum_w; return eta;}
float ClusterShapes::R(){ r = sum_r/sum_w; return r;}

float ClusterShapes::SigmaEtaEta(){return  sum_eta2/sum_w - Eta()*Eta();} 

float ClusterShapes::SigmaRR(){ return sum_r2/sum_w - R() *R();}


float ClusterShapes::SigmaPhiPhi(){ 
    float phi_0 = (sum_phi_0 / sum_w);
    float phi_1 = (sum_phi_1 / sum_w);
    float spp_0 = sum_phi2_0 / sum_w  - phi_0*phi_0;
    float spp_1 = sum_phi2_1 / sum_w  - phi_1*phi_1;

    if  (spp_0 < spp_1 )
    {
        phi = phi_0;
        isPhi0=true;
        while (phi < - M_PI) phi += 2*M_PI;
        while (phi >   M_PI) phi -= 2*M_PI;
        return spp_0;
    }
    else 
    {
        phi = phi_1 ;
        isPhi0=false;
        while (phi < - M_PI) phi += 2*M_PI;
        while (phi >   M_PI) phi -= 2*M_PI;
        return spp_1;
    }
}

float ClusterShapes::Phi(){
    SigmaPhiPhi(); //update phi
    return phi;
}


// off - diagonal
float ClusterShapes::SigmaEtaR(){ return -(sum_eta_r / sum_w - Eta() *R()) ;}

float ClusterShapes::SigmaEtaPhi(){
    SigmaPhiPhi() ; // decide which phi use, update phi

    if (isPhi0)
        return -(sum_eta_phi_0 /sum_w - Eta()*phi);
    else
        return -(sum_eta_phi_1 / sum_w - Eta()*phi);
}

float ClusterShapes::SigmaRPhi(){
    SigmaPhiPhi() ; // decide which phi use, update phi
    if (isPhi0)
        return -(sum_r_phi_0 / sum_w - R() *phi);
    else
        return -(sum_r_phi_1 / sum_w - R() * phi);
}

// -----------------------------------
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
