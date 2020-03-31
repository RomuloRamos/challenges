package com.example.listview;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.google.android.material.textfield.TextInputEditText;

import java.util.ArrayList;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {

    private ListView listLocais;
    private TextInputEditText txtInputSearch;
    private String strToCompare;
    private String[] strArrayItens = {"tesoura","faca","berinbal","bola", "anel", "avião", "cebola", "dado", "mesa", "australopiteco"};
    ArrayList<String> strNewArray = new ArrayList<String>();
    //Criar adaptador para a Lista
    ArrayAdapter<String> strArrayAdaptador;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listLocais = findViewById(R.id.listLocais);
        txtInputSearch = findViewById(R.id.txtInputSearch);

        strNewArray.addAll(Arrays.asList(strArrayItens));
        //Criar adaptador para a Lista
        strArrayAdaptador = new ArrayAdapter<String>(
                getApplicationContext(),android.R.layout.simple_list_item_1,
                android.R.id.text1,
                strNewArray);
        //Acionat Adaptador na Lista
        listLocais.setAdapter(strArrayAdaptador);

        txtInputSearch.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                //Acionat Adaptador na Lista
                listLocais.setAdapter(null);
                strNewArray.clear();
                strArrayAdaptador.clear();
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                strToCompare = txtInputSearch.getText().toString();
                setLists(strToCompare);
            }

            @Override
            public void afterTextChanged(Editable s) {
                strToCompare = txtInputSearch.getText().toString();
                if(strToCompare.compareTo("") == 0) {
                    listLocais.setAdapter(null);
                    strNewArray.addAll(Arrays.asList(strArrayItens));
                    listLocais.setAdapter(strArrayAdaptador);
                }
            }
        });
    }

    private void setLists(String strToCompare){

        int intCounter = 0;
        for(intCounter = 0; intCounter < strArrayItens.length; intCounter++){
            if (checkWordsTypos(strToCompare, strArrayItens[intCounter])){
                strNewArray.add(strArrayItens[intCounter]);
            }
        }
        if(strNewArray.size() != 0){
            listLocais.setAdapter(null);
            listLocais.setAdapter(strArrayAdaptador);
        }
        return;
    }

    private static boolean checkWordsTypos(String str1, String str2){
        int str1Lengh = str1.length();
        int str2Lengh = str2.length();
        if((Math.abs( str1Lengh - str2Lengh) > 1) || (str1Lengh == 0) || (str2Lengh == 0)){
            return false;
        }
//        boolean bInserError = false;
        boolean bRemoveError = false;
//        boolean bReplaceError = false;
        int intCount1 = 0;
        int intCount2 = 0;
        int intErrors = 0;
        int intMaxErrors = 1;
        if (str1Lengh < str2Lengh){
            intErrors++;
            bRemoveError = true;
        }
        while(intCount1 < str1Lengh) {
        // if last character was removed
            if(intCount2 >= str2Lengh) intErrors++;
            else if (str1.charAt(intCount1) != str2.charAt(intCount2)){
                intErrors++;
                if(intCount1+1 < str1Lengh){
                    char c1 = str1.charAt(intCount1+1);
                    char c2 = str2.charAt(intCount2);
                    if(c1 == c2){
                        if(bRemoveError){
                            bRemoveError = false;
                            intErrors--;
                        }
                        intCount1++;
                    }
                    if(intCount2+1 < str2Lengh) {
                        c1 = str1.charAt(intCount1);
                        c2 = str2.charAt(intCount2 + 1);
                        if (c1 == c2) {
                            if(bRemoveError){
                                bRemoveError = false;
                                intErrors--;
                            }
                            intCount2++;
                        }
                    }
                }
            }
            intCount1++;
            intCount2++;
            if(intErrors > intMaxErrors){
                return false;
            }
        }
//        if((str1Lengh >= str2Lengh) || (intErrors == 0)){
            return true;
//        }
//        return false;
    }
}
