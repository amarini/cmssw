#include "L1Trigger/L1THGCal/interface/UnionFind.h"

using namespace HGCalTriggerBackend;

std::size_t UF::Find(const std::size_t &i){
    if( forest_[i]  == i ) return i;
    std::size_t mypos = Find( forest_[i] );
    forest_[i] = mypos; // compress the search
    return mypos;
}

void UF::Union(std::size_t i, std::size_t j)
{
    i= Find(i);
    j= Find(j);
    if (i==j) return;
    if (size_ [i] > size_[j] ) {
        forest_[j] = i;
        size_[i] += size_[j];
    }
    else { 
        forest_[i] = j;
        size_[j] += size_[i];
    }
}

void UF::init(std::size_t N) 
{ 
    forest_.reserve(N); 
    size_.resize(N,1); 
    for(std::size_t i =0;i<forest_.size();++i) forest_[i]=i; 
    return;
}

void UF::add(std::size_t M){
    std::size_t N = size();
    forest_ . reserve( N + M) ; 
    size_ . reserve( N + M ) ;
    for(std::size_t i=0;i<M; ++i)
    {
        size_ . push_back(1);
        forest_ . push_back( N+i);
    }
}

void UF::merge( UF &x){ 
    std::size_t N2 = x.size();
    std::size_t N1 = this->size(); // this here is just for clarity
    forest_ . reserve ( N2 + N1 );
    size_   . reserve ( N2 + N1 );
    
    for (std::size_t i=0;i< N2;++i)
    {
        size_ . push_back( x.size_[i]);
        forest_ .push_back( x.forest_[i] +N1 ); // update to the new location
    }
    return ;
}


// -----------------------------------
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
