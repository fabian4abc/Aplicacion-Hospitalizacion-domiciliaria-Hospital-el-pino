import React, {Component} from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity, TextInput, TouchableHighlight} from 'react-native'
import { Divider } from 'react-native-elements';


class paciente extends Component{
    constructor(props){
        super(props)
        this.state = {
            nombre : '',
            rut : '',
            telefono : '',
            edad : ''            
        };
    };
    fetchData = async () => {
        const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/credenciales')
        const paciente = await response.json();
        var id_pac = this.props.navigation.state.params.id_paciente
        for (var i = 0; i < paciente.length; i++) {
            if (paciente[i].id == id_pac) {
                this.setState({ telefono: paciente[i].tel});
            }
        }
    }
    componentDidMount() {
        this.fetchData();
    }
    

    render(){        
        return(
        <View>
            <View style = {styles.container}>
                <Image style = {styles.logo1} source = {require("../assets/perfil.png")}></Image>
            </View>
            <Divider style = {{backgroundColor : "#696969", height : 3, marginTop : 200,marginEnd : 10, marginHorizontal : 7}}></Divider>
            <Text style = {styles.titleitem}>Nombre: {this.props.navigation.state.params.nombre}</Text>
            <Text style = {styles.titleitem}>Rut: {this.props.navigation.state.params.rut}</Text>
            <Text style = {styles.titleitem}>Domicilio: {this.props.navigation.state.params.domicilio}</Text>
            <TouchableOpacity style = {styles.button1} onPress = {() => this.props.navigation.navigate('Visita', this.props.navigation.state.params)} >
                  <Text style = {styles.buttontext1} > Historial de Visitas</Text>
            </TouchableOpacity>
            <View style = {styles.container}>
                <Image style = {styles.logo} source = {require("../assets/logo.png")}></Image>
            </View>
           

        </View>
        )
    }  
}
export default paciente
const styles = StyleSheet.create({
    form : {
        backgroundColor : 'white',
        marginVertical : 15,
        marginHorizontal : 10
        
    },
    textform : {
        paddingVertical : 5,
        paddingLeft : 5
        
    },
    titleitem : {
        marginVertical : 1,
        textAlign : "left",
        fontSize : 20,
        backgroundColor : "#808080",
        marginHorizontal : 10,
        color : "white",
        paddingLeft : 10
    },
    titleitem1 : {
        marginTop : 150,
        textAlign : "left",
        fontSize : 20,
        backgroundColor : "#808080",
        marginHorizontal : 10,
        color : "white",
        paddingLeft : 10
    },
    container : {
        flex : 1,
        flexDirection : 'column',    
        justifyContent : "flex-start",
        alignItems : "center",
    },
    logo1 : {    
        width : 150,
        height : 150,
        alignItems : "center",
        marginTop : 15,
        paddingEnd: 60
        
    },
    button1: {
        elevation: 10,
        backgroundColor: "#009688",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 10,
        marginVertical : 10,
        minWidth : "70%",
        borderRadius : 30,
        marginHorizontal : 20
    },
      buttontext1: {
        fontSize: 18,
        color: "#fff",
        fontWeight: "bold",
        alignSelf: "center",
        textTransform: "uppercase"
    },
    logo : {    
        width : 150,
        height : 150,
        justifyContent : "center",
        alignItems : "center",
        alignContent : "center"
    }

})