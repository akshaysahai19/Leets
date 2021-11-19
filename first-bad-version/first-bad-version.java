/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return getBadVersion(1,n,1);
    }
    
    public int getBadVersion(int left, int right, int last_bad){
        int mid = left + (right-left) / 2;
        // if(left==right&&isBadVersion(mid)){
        //     return mid;
        // }else if(left==right&&!isBadVersion(mid)){
        //     return last_bad;
        // }
        if(left>=right){
            return left;
        }
        
        if(isBadVersion(mid)){
            last_bad = mid;
            return getBadVersion(left,mid,last_bad);
        }else{
            return getBadVersion(mid+1,right,last_bad);
        }
    }
}