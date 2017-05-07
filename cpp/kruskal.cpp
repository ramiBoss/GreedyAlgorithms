#include<stdlib.h>
#include<iostream.h>

class edge{
public:
int src,des,weight;
};

class krk{
public:
int nodes,edges;
int path[10];
public :
void sort(edge[10],int);
void kruksal(edge[10]);
int checkcycle(edge);
};

void krk :: sort(edge e[10],int edges)
{
for(int i=0;i<edges;i++)
{
for(int j=1;j<edges-i-1;j++)
{
if(e[i].weight>e[j].weight){
int temp=e[i].weight;
e[i].weight=e[j].weight;
e[j].weight=temp;
}
}
}
}

void krk :: kruksal(edge e[]){
int path[10];

for(int i=0;i<nodes;i++)
path[i]=0;

for(i=0;i<edges;i++){
cout<<"Edge"<<e[i].src<<","<<e[i].des<<"is";
if(!checkcycle(e[i]))
cout<<"is selected";
else
cout<<"not selected";

}
}

int krk :: checkcycle(edge e){
int src=e.src,des=e.des;

while(path[src]>0)
src=path[src];

while(path[des]>0)
des=path[des];

if(src != des)
{
path[src]=des;
return 0;
}
return 1;
}

int main()
{
krk kruk;
int nodes,edges;
edge e[10];
cout<<"Enter the number of nodes";
cin>>nodes;
cout<<"Enter the number of edges";
cin>>edges;

for(int i=0;i<edges;i++){
cout<<"Inputs for edge"<<i;
cout<<"src";
cin>>e[i].src;
cout<<"des";
cin>>e[i].des;
cout<<"weight";
cin>>e[i].weight;
}
kruk.sort(e,edges);
kruk.kruksal(e);
return 0;
}
