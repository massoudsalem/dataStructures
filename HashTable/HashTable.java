public class HashTable<M,N>{
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

    private int capacity = 4;
    private int size;
    private Node table[];

    public HashTable(){
        table = new Node[capacity];
    }

    private int hash(M key){
        return key.hashCode() % capacity;
    }

    public void insert(M key, N value){
        int found = find(key);

        if(found != -1){
            table[found].setValue(value);
            return;
        }

        int hashedKey = hash(key), index = hashedKey, i = 0;
        while(table[index] != null && !table[index].isDeleted()){
            index = (hashedKey + i) % capacity;
            i++;
        }
        table[index] = new Node(key, value);
        size++;
        if(size > capacity/2)
            doubleCapacity();
        else if (size * 4 < capacity)
            halfenCapacity();
    }

    private void halfenCapacity() {
        this.capacity /= 2;
        Node oldTable[] = table.clone();
        this.table = new Node[capacity];
        for (Node e : oldTable) {
            if (e != null && !e.isDeleted())
                insert((M)e.getKey(), (N)e.getValue());
        }
    }

    private void doubleCapacity() {
        this.capacity *= 2;
        Node oldTable[] = table.clone();
        this.table = new Node[capacity];
        for (Node e : oldTable) {
            if (e != null && !e.isDeleted())
                insert((M)e.getKey(), (N)e.getValue());
        }
    }

    private int find(M key){
        int hashedKey = hash(key), index = hashedKey, i = 0;
        while(table[index] != null && table[index].getKey() != key){
            index = (hashedKey + i) % capacity;
            i++;
        }
        if(table[index] != null && !table[index].isDeleted() && table[index].getKey() == key)
            return index;
        return -1;
    }

    public N getValue(M key){
        int index = find(key);
        if(index != -1)
            return (N)table[index].getValue();
        return null;
    }

    public N remove(M key){
        int index = find(key);
        if(index != -1){
            N value = (N)table[index].getValue();
            table[index].delete();
            size--;
            if (size * 4 < capacity)
                halfenCapacity();
            return value;
        }
        System.out.println("key is not found!!");
        return null;
    }

    private String genStr(){
        StringBuilder stringBuilder = new StringBuilder();
        for(Node e:table){
            if(e != null && !e.isDeleted()){
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
        HashTable<String, Integer> hashTable = new HashTable<>();

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
