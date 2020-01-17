import java.util.LinkedList;

public class HashTable_Chaining<M,N>{
    class Node<M,N>{

        private M key;
        private N value;
        private boolean deleted = false;

        public Node(M key,N value){
            this.key = key;
            this.value = value;
        }

        public void delete(){
            this.deleted = true;
        }

        public boolean isDeleted(){
            return deleted;
        }

        public M getKey() {
            return key;
        }

        public N getValue() {
            return value;
        }

        public void setValue(N value) {
            this.value = value;
        }
    }

    private final int capacity = 128;
    private LinkedList<Node<M, N>> table[];

    public HashTable_Chaining(){
        table = new LinkedList [capacity];
    }

    private int hash(M key){
        return key.hashCode() % capacity;
    }



    public void insert(M key, N value){
        Node found = find(key);
        if(found != null){
            found.setValue(value);
            return;
        }
        int hashedKey = hash(key);
        if(table[hashedKey] == null)
            table[hashedKey] = new LinkedList<>();
        table[hashedKey].add(new Node(key, value));
    }


    private Node find(M key){
        int hashedKey = hash(key);
        if(table[hashedKey] == null)
            return null;

        for(Node e:table[hashedKey]){
            if(e.key == key)
                return e;
        }

        return null;
    }

    public N getValue(M key){
        Node node = find(key);
        if(node != null)
            return (N)node.getValue();
        return null;
    }

    public N remove(M key){
        Node node = find(key);
        N value = null;
        if(node != null){
            value = (N)node.getValue();
            int hashedKey = hash(key);
            table[hashedKey].remove(node);
        }
        if(value == null)
            System.out.println("key is not found!!");
        return value;
    }

    private String genStr(){
        StringBuilder stringBuilder = new StringBuilder();
        for(LinkedList L:table){
            if(L == null)
                continue;
            for(Object a:L){
                Node e = (Node)a;
                stringBuilder.append(String.format("%s : %s, ", e.getKey(), e.getValue()));
            }
        }
        if (stringBuilder.length() > 1) {
            stringBuilder.setLength(stringBuilder.length() - 2);
        }
        return stringBuilder.toString();
    }

    @Override
    public String toString() {
        return "[" + genStr() + "]";
    }

    public static void main(String args[]){
        HashTable_Chaining<String, Integer> hashTable = new HashTable_Chaining<>();

        hashTable.insert("map1", 1);
        System.out.println(hashTable);
        hashTable.insert("map2", 2);
        System.out.println(hashTable);
        hashTable.insert("map3", 3);
        System.out.println(hashTable);
        hashTable.insert("map4", 4);
        System.out.println(hashTable);

        System.out.println(hashTable.remove("map1"));
        System.out.println(hashTable);

        hashTable.insert("map1",1);
        System.out.println(hashTable);
        hashTable.insert("map5",5);
        System.out.println(hashTable);
        hashTable.insert("map6",6);
        System.out.println(hashTable.getValue("map5"));
        System.out.println(hashTable);
        hashTable.remove("map7");
        System.out.println(hashTable);
        hashTable.remove("map5");
        System.out.println(hashTable);
        hashTable.remove("map2");
        System.out.println(hashTable);
        hashTable.remove("map1");
        System.out.println(hashTable);
        hashTable.remove("map6");
        System.out.println(hashTable);
        hashTable.remove("map3");
        System.out.println(hashTable);
        hashTable.remove("map4");
        System.out.println(hashTable);
        System.out.println(hashTable.getValue("map8"));
        hashTable.insert("map1",12);
        System.out.println(hashTable);
        hashTable.insert("map1",16);
        System.out.println(hashTable);
        hashTable.remove("map1");
        System.out.println(hashTable);
        hashTable.insert("map1",13);
        System.out.println(hashTable);
    }
}
