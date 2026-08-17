class Solution {
    public int candy(int[] ratings) {
        int[] candy = new int[ratings.length];
        int count =0;
       for(int i=0;i < candy.length;i++){
            candy[i] =1;
        }
        for(int j=1;j <candy.length;j++){
            if(ratings[j-1] < ratings[j]){
                candy[j] = candy[j-1]+1;
            }
        }
        for(int j=candy.length-2; j >=0;j--){
            if(ratings[j+1] < ratings[j]){
                candy[j] =Math.max(candy[j],candy[j+1]+1);
            }
        }
        for(int k=0;k<candy.length;k++){
            count +=candy[k];
        }
        return count;
    }
}