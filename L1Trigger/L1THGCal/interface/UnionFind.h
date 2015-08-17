#include <vector>
#include <map>
#include <unordered_map>

namespace HGCalTriggerBackend{
    // standard UF
    
    class UF{
        private:
            // forest
            std::vector<std::size_t>   forest_; 
            std::vector<std::size_t>   size_; 

        public:
            // find of the union find , using only the forest
            std::size_t Find(const std::size_t &i);

            void Union(std::size_t i, std::size_t j);

            // void init
            inline std::size_t size() { return forest_.size(); }
            inline bool empty() { return forest_.empty(); }
            inline virtual void reset(){forest_.clear(); size_.clear();}
            virtual void init(std::size_t N);             
            // make it grow 
            virtual void add(std::size_t M=1);
            // make it parallel: merge two UF structures
            virtual void merge(UF &x);

    };

    template<typename TYPE>
        class UFMap: private UF { // avoid that user have access to the direct UF members.
            private:
                // navigate through the types
                std::vector<TYPE> id_map;    
                std::unordered_map<TYPE, std::size_t>  inv_map;

            protected:
                const std::vector<TYPE> GetIdMap() const  { return id_map;}
                const std::unordered_map<TYPE, std::size_t> GetInvMap() const { return inv_map;}

            public:
                TYPE Find (TYPE &a)
                {
                    // locate the original position inside the forest
                    std::size_t pos = inv_map[ a ] ;
                    std::size_t find = UF::Find( pos );
                    return id_map[ pos ];
                } 
                void Union( const TYPE &a , const TYPE &b)
                {
                    std::size_t x = inv_map[ a ] ;
                    std::size_t y = inv_map[ b ] ;
                    UF::Union( a, b);
                }
                //
                bool search(TYPE&a)
                {
                    if ( inv_map.find( a) != inv_map.end() ) { return true;} // already there
                    return false;
                }

                virtual bool add(TYPE &a)
                {
                    if ( search(a) ) return false;
                    std::size_t n= UF::size();  // assert id_map.size() == uf.size();
                    id_map.push_back( a ); 
                    inv_map[a] = n;
                    UF::add();
                    return true;
                }

                inline virtual void reset(){ UF::reset() ; id_map.clear() ; inv_map.clear(); }

                virtual void merge( UFMap<TYPE> &x ) 
                {
                    std::size_t N1 = size();
                    std::size_t N2 = x.size();

                    id_map . reserve(N1+N2);
                    
                    for(int i=0;i< N2 ;++i)
                    {
                        TYPE a = x.inv_map[a];
                        id_map.push_back(a);
                        inv_map[a] = i+N1;
                    }
                    // merge the underlying structure
                    UF::merge( x );
                }
        };

    template <typename TYPE, typename DATA>
        class UFCluster : public UFMap<TYPE>{

            std::vector<DATA> value;     // associative container with an extra value like the energy

            public:
            DATA get(TYPE&a)
            {
                TYPE b = Find(a); // only the greatest
                std::size_t pos = this->GetInvMap()[b];
                return value[pos];
            }

            bool add(TYPE &a,DATA &d) {
                std::size_t n = this->size();
                if (not UFMap<TYPE>::add(a)) return false;
                value[n] = d;
                return true;
            }

            void Union(TYPE&a ,TYPE&b)
            { 
                Union(a,b, [] (const DATA &d1, const DATA &d2 ) -> DATA { return d1+d2;} );
            }

            void Union( TYPE &a , TYPE &b, const DATA (*Sum)(const DATA &d1, const DATA &d2) )
            {
                DATA d1 = get(a);
                DATA d2 = get(b);
                UFMap<TYPE>::Union(a,b);
                TYPE c = Find(a);
                std::size_t pos = this->GetInvMap()[c];
                value [ c ] = Sum(d1,d2);
            }

            void merge( UFCluster<TYPE,DATA> &x )
            {
                std::size_t N1 = this->size();
                std::size_t N2 = x.size();
                //std::vector<DATA> value; 
                value . reserve ( N1 + N2 );
                for( int i=0;i< N2 ;++i)
                    value.push_back( x[i] ) ;
            // merge the underlying structure 
                UFMap<TYPE>::merge(x);
            }
        };

};

// -----------------------------------
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
