import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> adjVector = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<=n; i++)
            adjVector.add(new ArrayList<Integer>());
        for(int[] current : edge){
            int a = current[0];
            int b = current[1];
            adjVector.get(a).add(b);
            adjVector.get(b).add(a);
        }
        boolean visited[] = new boolean[n+1];
        for(int i=0; i<visited.length; i++)
            visited[i] = false;

        Queue<Integer> q = new LinkedList<>();

        int count = 0;
        q.offer(1);
        visited[1] = true;
        while(!q.isEmpty()){
            int length = q.size();
            count = length;
            while(length > 0){
                length -= 1;
                int current = q.peek();
                q.poll();
                for(int target : adjVector.get(current)){
                    if(!visited[target]){
                        q.offer(target);
                        visited[target] = true;
                    }
                }
            }
        }

        answer = count;
        return answer;
    }
}