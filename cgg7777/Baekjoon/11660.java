import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] accArray = new int[N+1][N+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<N+1; j++){
                accArray[i][j] = accArray[i][j-1] + Integer.parseInt(st.nextToken());
            }
        }
        String[] answerArr = new String[M];
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int xStart = x1;
            int xFinish = x2;

            int yStart = y1;
            int yFinish = y2;

            int acc = 0;
            for(int j=xStart; j<=xFinish; j++){
                acc += accArray[j][yFinish] - accArray[j][yStart-1];
            }
            answerArr[i] = Integer.toString(acc);
        }

        for(String answer: answerArr)
            System.out.println(answer);
    }
}
