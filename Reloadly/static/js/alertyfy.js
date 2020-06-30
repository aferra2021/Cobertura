<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
	
	>
<channel>
	<title>Comentarios en: Creando mejores alertas y cuadros de diálogo con AlertifyJS</title>
	<atom:link href="http://www.falconmasters.com/javascript/alertas-alertifyjs/feed/" rel="self" type="application/rss+xml" />
	<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/</link>
	<description>Blog de Diseño Web, Tutoriales, Cursos, Recursos, Código</description>
	<lastBuildDate>Thu, 08 Mar 2018 18:24:00 +0000</lastBuildDate>
	<sy:updatePeriod>hourly</sy:updatePeriod>
	<sy:updateFrequency>1</sy:updateFrequency>
	<generator>https://wordpress.org/?v=4.9.15</generator>
	<item>
		<title>Por: Kathia rodriguez ortiz</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-3429</link>
		<dc:creator><![CDATA[Kathia rodriguez ortiz]]></dc:creator>
		<pubDate>Wed, 23 Aug 2017 16:44:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-3429</guid>
		<description><![CDATA[Hola Falcon, quiero aplicar el alertify para eliminar un registro al dar Ok, lo estoy realizando c on una function algo como esto: 

function confirmar(){ 
                                    confirmar=confirm(&quot;¿Esta seguro que desea eliminar el registro seleccionado?&quot;); 
                                    if (confirmar) 
                                        quitarCE();
                                    else 
                                        return false; 
                                    } 
y luego desde un btn llamo a la función. 

Pero al crearlo con el alertify tengo algo como esto y no lo logro.,,, 

 var msg = alertify.confirm(&quot;¿Esta seguro que desea eliminar el registro seleccionado?&quot;, null, null, null).set({Ok:&#039;Confirmar&#039;,cancel:&#039;Cancelar&#039;});
                                    msg.callback = function (confirmar){
                                        
                                        if (confirmar)
                                            quitarCE();
                                        else
                                            return false;
                                    }]]></description>
		<content:encoded><![CDATA[<p>Hola Falcon, quiero aplicar el alertify para eliminar un registro al dar Ok, lo estoy realizando c on una function algo como esto: </p>
<p>function confirmar(){<br />
                                    confirmar=confirm(«¿Esta seguro que desea eliminar el registro seleccionado?»);<br />
                                    if (confirmar)<br />
                                        quitarCE();<br />
                                    else<br />
                                        return false;<br />
                                    }<br />
y luego desde un btn llamo a la función. </p>
<p>Pero al crearlo con el alertify tengo algo como esto y no lo logro.,,, </p>
<p> var msg = alertify.confirm(«¿Esta seguro que desea eliminar el registro seleccionado?», null, null, null).set({Ok:&#8217;Confirmar&#8217;,cancel:&#8217;Cancelar&#8217;});<br />
                                    msg.callback = function (confirmar){</p>
<p>                                        if (confirmar)<br />
                                            quitarCE();<br />
                                        else<br />
                                            return false;<br />
                                    }</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Reinier Garcia Ramos</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-3209</link>
		<dc:creator><![CDATA[Reinier Garcia Ramos]]></dc:creator>
		<pubDate>Sat, 22 Apr 2017 02:25:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-3209</guid>
		<description><![CDATA[Tecleas esto en el header, por ejemplo:



        &lt;!-- Alertify: include the core styles --&gt;
        

        &lt;!-- Alertify: include a theme, can be included into the core instead of using 2 separate files (like now) --&gt;
        

   





        &lt;!-- Dirección del fichero .js del plugin Alertify --&gt;
        ]]></description>
		<content:encoded><![CDATA[<p>Tecleas esto en el header, por ejemplo:</p>
<p>        <!-- Alertify: include the core styles --></p>
<p>        <!-- Alertify: include a theme, can be included into the core instead of using 2 separate files (like now) --></p>
<p>        <!-- Dirección del fichero .js del plugin Alertify --></p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Reinier Garcia Ramos</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-3208</link>
		<dc:creator><![CDATA[Reinier Garcia Ramos]]></dc:creator>
		<pubDate>Sat, 22 Apr 2017 02:22:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-3208</guid>
		<description><![CDATA[Debes ponerle, por ejemplo: 

alertify.alert(&#039;Hola&#039; + &#039;&#039; + &#039;mundo&#039;);

Lo que el objeto alertify está recibiendo en sus funciones alert, promt y confirm es puro html.]]></description>
		<content:encoded><![CDATA[<p>Debes ponerle, por ejemplo: </p>
<p>alertify.alert(&#8216;Hola&#8217; + » + &#8216;mundo&#8217;);</p>
<p>Lo que el objeto alertify está recibiendo en sus funciones alert, promt y confirm es puro html.</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Raynex</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-3153</link>
		<dc:creator><![CDATA[Raynex]]></dc:creator>
		<pubDate>Sun, 19 Mar 2017 13:49:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-3153</guid>
		<description><![CDATA[Amigo, todo funciona bien, pero como puedo hacer un salto de linea  en las alertas? en las alertas normales usaba el \n pero el alertify al parecer no lo reconoce]]></description>
		<content:encoded><![CDATA[<p>Amigo, todo funciona bien, pero como puedo hacer un salto de linea  en las alertas? en las alertas normales usaba el \n pero el alertify al parecer no lo reconoce</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Andres Rivero</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-2858</link>
		<dc:creator><![CDATA[Andres Rivero]]></dc:creator>
		<pubDate>Wed, 19 Oct 2016 22:37:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-2858</guid>
		<description><![CDATA[Cómo hago para que funcione eso? osea lo descarge ahora que? ¿que tengo que hacer para ponerlo en funcionamiento?]]></description>
		<content:encoded><![CDATA[<p>Cómo hago para que funcione eso? osea lo descarge ahora que? ¿que tengo que hacer para ponerlo en funcionamiento?</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Rafael Rodriguez</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-1813</link>
		<dc:creator><![CDATA[Rafael Rodriguez]]></dc:creator>
		<pubDate>Mon, 12 Oct 2015 01:40:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-1813</guid>
		<description><![CDATA[Muchas gracias! Tu blog esta montado con wordpress? Imagino no vale la pena ponerme a programar en php si wordpress ofrece todo hecho, pero Me preocupa que wordpress sea pesado y sobrecargue el servidor.]]></description>
		<content:encoded><![CDATA[<p>Muchas gracias! Tu blog esta montado con wordpress? Imagino no vale la pena ponerme a programar en php si wordpress ofrece todo hecho, pero Me preocupa que wordpress sea pesado y sobrecargue el servidor.</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Carlos Arturo</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-1685</link>
		<dc:creator><![CDATA[Carlos Arturo]]></dc:creator>
		<pubDate>Thu, 10 Sep 2015 19:43:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-1685</guid>
		<description><![CDATA[No, es gratiuto, solo que tienes que buscar el plugin para la plataforma que usas por ejemplo el plugin para wordpress.]]></description>
		<content:encoded><![CDATA[<p>No, es gratiuto, solo que tienes que buscar el plugin para la plataforma que usas por ejemplo el plugin para wordpress.</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Rafael Rodriguez</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-1684</link>
		<dc:creator><![CDATA[Rafael Rodriguez]]></dc:creator>
		<pubDate>Thu, 10 Sep 2015 19:31:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-1684</guid>
		<description><![CDATA[Gracias por la info. Imagino disqus.com es de pago? Entre en el sitio y no vi como contratar ese servicio. ]]></description>
		<content:encoded><![CDATA[<p>Gracias por la info. Imagino disqus.com es de pago? Entre en el sitio y no vi como contratar ese servicio. </p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Carlos Arturo</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-1680</link>
		<dc:creator><![CDATA[Carlos Arturo]]></dc:creator>
		<pubDate>Tue, 08 Sep 2015 23:02:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-1680</guid>
		<description><![CDATA[Es con el servicio de disqus.com]]></description>
		<content:encoded><![CDATA[<p>Es con el servicio de disqus.com</p>
]]></content:encoded>
	</item>
	<item>
		<title>Por: Rafael Rodriguez</title>
		<link>http://www.falconmasters.com/javascript/alertas-alertifyjs/#comment-1679</link>
		<dc:creator><![CDATA[Rafael Rodriguez]]></dc:creator>
		<pubDate>Tue, 08 Sep 2015 15:51:00 +0000</pubDate>
		<guid isPermaLink="false">http://www.falconmasters.com/?p=1013#comment-1679</guid>
		<description><![CDATA[FalconMasters, cómo se hace para agregar esta funcionalidad de comentarios con integracion de redes sociales?]]></description>
		<content:encoded><![CDATA[<p>FalconMasters, cómo se hace para agregar esta funcionalidad de comentarios con integracion de redes sociales?</p>
]]></content:encoded>
	</item>
</channel>
</rss>