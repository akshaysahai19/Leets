class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        pos_domains = []
        domain_dict = {}
        for domains_count in cpdomains:
            count = int(domains_count.split(" ")[0])
            domain = str(domains_count.split(" ")[1])
            only_domains = domain.split(".")
            
            
            if(len(only_domains)>2):
                pos_domains.append(str(only_domains[0])+"."+str(only_domains[1])+"."+str(only_domains[2]))
                pos_domains.append(str(only_domains[1])+"."+str(only_domains[2]))
                pos_domains.append(str(only_domains[2]))
            else:
                pos_domains.append(str(only_domains[0])+"."+str(only_domains[1]))
                pos_domains.append(str(only_domains[1]))
            
            for possible in pos_domains:
                if possible in domain_dict:
                    domain_dict[possible] = domain_dict[possible] + count
                else:
                    domain_dict[possible] = count
            pos_domains = []
                
        output = []
        for key in domain_dict:
            val = ""+str(domain_dict[key])+" "+str(key)
            output.append(val)
            
        return output
        
            
        