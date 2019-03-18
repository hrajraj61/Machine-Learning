# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:58:09 2019

@author: hrajr
"""

def find(dna,N):
    s=set()
    n=len(dna)
    dic={}
    for i in range(n-N):
        tmp=dna[i:i+N]
        dic[tmp]=dic.get(tmp,0)+1
    for k in dic.keys():
        if(dic[k]>1):
            s.add(k)
    for st in sorted(s):
        print(st)
    if(len(s)==0):
      print("None")
n,dna=int(input()),input()

#('AACAAAAACAAAACCAAAAACAAAAACAAAA',3)

find(dna,n)




"""
package test;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

/**
 *
 * @author nik260
 */
public class CodevitaD {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        Set<String> set = new TreeSet<String>();
        Map<String,Integer> allSubstings=new HashMap<>();
        String str = sc.nextLine();
        for (int i = 0; i <= str.length() - N; i++) {
            String temp = str.substring(i, i + N);
            Integer temp1=allSubstings.get(temp);
            if(temp1==null)
                allSubstings.put(temp, 1);
            else
                allSubstings.put(temp, temp1+1);
        }
        for (String set1 : allSubstings.keySet()) {
            Integer tempint=allSubstings.get(set1);
            if(tempint>1)
                set.add(set1);
        }
        int t = 0;
        for (String set1 : set) {
            if (set.size() != t) {
                System.out.print(set1 + "\n");
            } else {
                System.out.print(set1);
            }
            t++;
        }

        if (set.size()== 0) {
            System.out.print("None");
        }
    }

}"""