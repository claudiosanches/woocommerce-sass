WooCommerce Compass
===================

WooCommerce Styles with Compass/SASS

## Requirements ##

* Compass/SASS

## Installation ##

Add the files in the folder of your theme keeping this structure.

Run the following command to generate the css file:

    $ compass compile

Paste in your functions.php:

    function cs_woocommerce_compass() {
        wp_register_style( 'woocommerce-compass', get_template_directory_uri() . '/css/woocommerce.css', array(), false, 'all' );

        wp_enqueue_style( 'woocommerce-compass' );
    }
    add_action( 'wp_enqueue_scripts', 'cs_woocommerce_compass' );

Now in the WooCommerce settings just deactivate the CSS.
