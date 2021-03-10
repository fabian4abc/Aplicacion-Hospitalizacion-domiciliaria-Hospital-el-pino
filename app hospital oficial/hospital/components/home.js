import {Component} from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity} from 'react-native'
import React from 'react'


class home extends Component{
  saludo = () => {Alert.alert("Wena CTM!")}
  fventas = () => {
    this.saludo;
    //this.props.navigation.navigate('ventas')
    //console.log("paso aqui :c");    
  }
  render(){    
    return(      
        <View style = {styles.container}>
            <View style = {styles.buttoncontainer}>             
              <TouchableOpacity style = {styles.button1} onPress = {() => this.props.navigation.navigate('VisitasAsignadas')} >
                  <Text style = {styles.buttontext1} > Vistas asignadas</Text>
              </TouchableOpacity>
              <TouchableOpacity style = {styles.button1} onPress = {() => this.props.navigation.navigate('Mapa')} >
                  <Text style = {styles.buttontext1}>iniciar ruta</Text>
              </TouchableOpacity>
              <TouchableOpacity style = {styles.button1} onPress = {() => this.props.navigation.navigate('Perfil',  this.props.navigation.state.params)}>
                  <Text style = {styles.buttontext1}>ver perfil</Text>
              </TouchableOpacity>                      
              <Image style = {styles.logo} source = {require("../assets/logo.png")}></Image>
            </View>
            
        </View>     
        
    )
  }
}
const styles = StyleSheet.create({
  container : {
    flex : 1,
    flexDirection : 'column'    
  },
  buttoncontainer : {
    flex : 5,
    flexDirection : 'column',
    justifyContent : "flex-start",
    alignItems : "center",
    marginTop : 60
    
  },
  logo : {    
    width : 300,
    height : 300,
    justifyContent : "center",
    alignItems : "center",
    alignContent : "center"
  },  
  button1: {
    elevation: 10,
    backgroundColor: "#009688",
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 10,
    marginVertical : 10,
    minWidth : "70%",
    borderRadius : 30
  },
  buttontext1: {
    fontSize: 18,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  negrita : {
    fontWeight : "bold"
  },
  header : {    
    flex : 0.05,
    flexDirection : 'row',
    marginTop : 40,
    justifyContent : "center",
    alignItems : "center",
    backgroundColor : "#c1bfbf"
  },
  body : {
    flex : 0.2,
    alignItems : 'center',
    marginBottom : 150,
    marginTop : 0
  },
  footer : {
    flex : 0.5,
    alignItems : 'center',
    justifyContent : "flex-end",
    position: "relative",
    bottom: 0,    
  }
})

export default home