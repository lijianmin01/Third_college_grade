public class rw03{

    public static void main(String[] args){
        try{
            while(true){
                int N,R,Q;
                N = nextInt();
                R = nextInt();
                Q = nextInt();

                Player[] all=new Player[2*N];

                Player[] win=new Player[N];
                Player[] losser=new Player[N];
                for(int i = 0;i<2*N;i++){
                    int s=nextInt();
                    int id=i+1;
                    all[i]=new Player(id,s);
                }

                for(int i = 0;i<2*N;i++){
                    all[i].w = nextInt();
                }

                //模拟比赛
                Arrays.sort[all];

                for(int i = 0;i<R;i++){
                    for (int j = 0;j<N;j++){
                        if (all[2*j].w>all[2*j+1].w){
                            win[j]=all[2*j];
                            losser[j]=all[2*j+1];
                        }else{
                            win[j]=all[2*j+1];
                            losser[j]=all[2*j];
                        }
                        win[j].s++;
                    }
                    //合并
                    int w=0,l=0,a=0;
                    while(w<win.length && l<losser.length){
                        if(win[w].s>losser[l].s || (win[w].s==losser[l].s && win[w].id<losser[l].id )){
                            all[a++] = win[w++];
                        }else{
                            all[a++] = losser[l++];
                        }
                    }

                    while(w<win.length){
                        all[a++]=win[w++];
                    }
                    while(l<losser.length){
                        all[a++]=losser[l++];
                    }
                }

                System.out.println(all[Q-1].id);
            }
            

        }catch(Exception e){
            return 0;
        }

    }


}

// 定义选手对象
class Player implements Comparable<Player>{
    int id;
    int w;
    int s;

    //创建一个构造器
    public Player(int id,int s){
        this.id = id;
        this.s = s;
    }

    @Override
    public int Comparable(Player o){
        if(this.s==o.s){
            return Integer.compare(this.id,o.id);
        }else{
            return  Integer.compare(o.s,this.s);
        }
    }
}