import java.util.*;
class Solution {
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = {};
        Arrays.sort(summits);
        HashSet<Integer> summitSet = new HashSet<Integer>();
        HashSet<Integer> gateSet = new HashSet<Integer>();
        for(int summit : summits) summitSet.add(summit);
        for(int gate : gates) gateSet.add(gate);

        ArrayList<ArrayList<ArrayList<Integer>>> adjVector = new ArrayList<ArrayList<ArrayList<Integer>>>();

        for(int i=0; i<n+1; i++){
            adjVector.add(new ArrayList<ArrayList<Integer>>());
        }

        for(int[] path : paths){
            adjVector.get(path[0]).add(new ArrayList<Integer>(Arrays.asList(path[1], path[2])));
            adjVector.get(path[1]).add(new ArrayList<Integer>(Arrays.asList(path[0], path[2])));
        }

        int maxNum = paths[0][2];
        for(int[] path : paths){
            if(maxNum < path[2]) maxNum = path[2];
        }

        int left = 1;
        int right = maxNum;
        while(left <= right){
            int mid = (left + right) / 2;
            int tempSummit = 0;
            boolean okFlag = false;
            for(int summit : summits){
                Queue<Integer> queue = new LinkedList<Integer>();
                boolean[] visited = new boolean[n+1];
                for(int i=0; i< n+1; i++){
                    visited[i] = false;
                }
                queue.offer(summit);
                visited[summit] = true;
                while(!queue.isEmpty()){
                    int size = queue.size();
                    while(size >0){
                        size -= 1;
                        int current = queue.peek();

                        queue.poll();
                        if(gateSet.contains(current)){
                            okFlag = true;
                            break;
                        }
                        for(ArrayList<Integer> edge : adjVector.get(current)){
                            if(edge.get(1) <= mid && !visited[edge.get(0)] && !summitSet.contains(edge.get(0))){
                                queue.offer(edge.get(0));
                                visited[edge.get(0)] = true;
                            }
                        }
                    }
                }

                if(okFlag) {
                    tempSummit = summit;
                    break;
                }

            }
            if(okFlag){
                int[] answerCandidate = {tempSummit, mid};
                answer = answerCandidate;
                right = mid -1;
            }
            else{
                left = mid +1;
            }
        }
        return answer;
    }
}