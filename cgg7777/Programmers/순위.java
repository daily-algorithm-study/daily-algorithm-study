import java.util.*;
class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;

        int[][] floydWashall = new int[n+1][n+1];
        for(int i=0; i<n+1; i++){
            for(int j=0; j<n+1; j++){
                floydWashall[i][j] = 0;
            }
        }

        for(int[] currentBattle : results){
            int a = currentBattle[0];
            int b = currentBattle[1];
            floydWashall[a][b] = 1;
            floydWashall[b][a] = -1;
        }

        for(int i=1; i<n+1; i++){
            for(int j=1; j<n+1; j++){
                for(int k=1; k<n+1; k++){
                    if(floydWashall[j][i] == 1 && floydWashall[i][k] == 1)
                        floydWashall[j][k] = 1;
                    else if (floydWashall[j][i] == -1 && floydWashall[i][k] == -1)
                        floydWashall[j][k] = -1;
                }
            }
        }
        for(int i=1; i<n+1; i++){
            boolean okflag = false;
            for(int j=1; j<n+1; j++){
                if( i != j && floydWashall[i][j] == 0){
                    okflag = true;
                    break;
                }
            }
            if(!okflag)
                answer +=1;
        }
        return answer;
    }
}