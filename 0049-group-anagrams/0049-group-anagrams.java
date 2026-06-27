class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

      HashMap<String, List<String>> mp = new HashMap<>();  

      for(String s : strs)  
      {
        char arr[] = s.toCharArray();
        Arrays.sort(arr);
        String str = new String(arr);

        if(!mp.containsKey(str))
        {
            mp.put(str, new ArrayList<>());
        }
        mp.get(str).add(s); //Using add as the map.get() here will return a list.
      }

      return new ArrayList<>(mp.values());
    }
}