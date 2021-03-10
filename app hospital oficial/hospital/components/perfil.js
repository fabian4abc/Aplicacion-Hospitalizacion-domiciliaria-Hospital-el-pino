import React, { Component } from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity, TextInput, TouchableHighlight } from 'react-native'
import { createAppContainer } from 'react-navigation'
import { createStackNavigator } from 'react-navigation-stack'


class perfil extends Component {

    constructor(props) {
        super(props)
        this.state = {
            personal: [],
            especialidad: [],
            loading: true
        };
    };

    fetchData = async () => {
        /*let myHeaders = new Headers();
        var data = {username: '3'}
        const options = {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {
                'Content-Type': 'application/json'
            }
        }*/
        const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/perfil');
        const response1 = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/personal');
        const personal = await response.json();
        const especialidad = await response1.json();
        const id_personal = this.props.navigation.state.params.usuario_id;
        for (var i = 0; i < personal.length; i++) {
            if (personal[i].id == id_personal) {
                this.setState({ personal: personal[i]});
            }
        }
        for (var i = 0; i < especialidad.length; i++) {
            if (especialidad[i].id_perfil_id == id_personal) {
                this.setState({ especialidad: especialidad[i], loading: false });
            }
        }
    }
    componentDidMount() {
        this.fetchData();
    }


    render() {
        return (
            <View>
                <View style={styles.columna}>
                    <Image style={styles.logo} source={require("../assets/perfil.png")}></Image>
                    <Text style={styles.texto}>{this.state.personal.first_name} {this.state.personal.last_name}</Text>
                    <Text style={styles.texto}>{this.state.especialidad.especialidad}</Text>
                </View>
                <Text style={styles.texto1}> {this.state.especialidad.rut} </Text>
                <Text style={styles.texto1}> {this.props.navigation.state.params.tel}</Text>
                <Text style={styles.texto2}> {this.state.personal.email}</Text>
                <TouchableOpacity style={styles.button1} onPress={() => this.props.navigation.navigate('EditarPerfil',this.props.navigation.state.params)}>
                    <Text style={styles.buttontext1}>Editar perfil</Text>
                </TouchableOpacity>
                <View style={styles.container}>
                    <Image style={styles.logo1} source={require("../assets/logo.png")}></Image>
                </View>
            </View>

        )
    }
}
export default perfil
const styles = StyleSheet.create({
    columna: {
        flexDirection: "row",
        flex: 1,
        alignItems: "center",
        marginTop: 100
    },
    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: "flex-start",
        alignItems: "center",
    },
    texto: {
        paddingHorizontal: 15,
        textAlign: "center",
        fontSize: 20,
    },
    texto1: {
        paddingHorizontal: 15,
        fontSize: 20,
        paddingTop: 25
    },
    texto2: {
        paddingHorizontal: 15,
        fontSize: 20,
    },
    logo: {
        width: 150,
        height: 150,
        marginLeft: 20,
        marginVertical: 15,
    },
    logo1: {
        width: 150,
        height: 150,
        alignItems: "center",
        marginTop: -10
    },
    form: {
        backgroundColor: 'white',
        marginVertical: 15,
        marginHorizontal: 10

    },
    textform: {
        paddingVertical: 5,
        paddingLeft: 5

    },
    titleitem: {
        marginBottom: -10
    },
    button1: {
        elevation: 10,
        backgroundColor: "#009688",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 10,
        marginVertical: 10,
        marginHorizontal: 40,
        minWidth: "70%",
        borderRadius: 30
    },
    buttontext1: {
        fontSize: 18,
        color: "#fff",
        fontWeight: "bold",
        alignSelf: "center",
        textTransform: "uppercase"
    }

})