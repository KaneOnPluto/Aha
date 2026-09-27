def extract_sublist(original_list,s_index,e_index):
    sublist=original_list[s_index:e_index]

    return sublist

if __name__ =="__main__":

    mainlist=[1,2,3,4,5,6,7,8]
    start_index=2
    end_index=6

    sublist=extract_sublist(mainlist,start_index,end_index)

    print("original list-->",mainlist)
    print("sublist--->",sublist)
