import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Polygon;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;


public class Main extends Application {

    /** Scene constants */
    private final static double SCENE_WIDTH = 450.0;
    private final static double SCENE_HEIGHT = 275.0;
    private final static Color DEFAULT_SCENE_COLOR = Color.rgb(255, 255, 130);

    /** Sail constants */
    private final static Color DEFAULT_SAIL_COLOR = Color.LIGHTGRAY;
    private final static double[] SAIL_POINTS = new double[] {
            152.0, 80.0,
            185.0, 16.0,
            286.0, 16.0,
            268.0, 92.0,
            294.0, 144.0,
            170.0, 144.0
    };

    /** Mast constants */
    private final static double MAST_POINT_X = 218.0;
    private final static double MAST_POINT_Y = 144.0;
    private final static double MAST_WIDTH = 12.0;
    private final static double MAST_HEIGHT = 60.0;

    /** Hull constants */
    private final static Color DEFAULT_HULL_COLOR = Color.SADDLEBROWN;
    private final static double[] HULL_POINTS = new double[] {
            39.0, 163.0,
            181.0, 204.0,
            304.0, 204.0,
            395.0, 159.0,
            315.0, 264.0,
            168.0, 264.0
    };

    @Override
    public void start(Stage primaryStage) throws Exception {
        Group root = new Group();
        Scene scene = new Scene(root, SCENE_WIDTH,
                SCENE_HEIGHT, DEFAULT_SCENE_COLOR);

        addSailToRoot(root);
        addMastToRoot(root);
        addHullToRoot(root);

        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String [] args) {
        launch(args);
    }

    private void addSailToRoot(Group root) {
        addPolygonToRoot(root, SAIL_POINTS, DEFAULT_SAIL_COLOR);
    }

    private void addHullToRoot(Group root) {
        addPolygonToRoot(root, HULL_POINTS, DEFAULT_HULL_COLOR);
    }

    private void addPolygonToRoot(Group root, double[] points, Color color) {
        Polygon polygon = new Polygon(points);
        polygon.setFill(color);

        root.getChildren().add(polygon);
    }

    private void addMastToRoot(Group root) {
        Rectangle mast = new Rectangle(MAST_POINT_X, MAST_POINT_Y,
                MAST_WIDTH, MAST_HEIGHT);
        mast.setFill(Color.BLACK);

        root.getChildren().add(mast);
    }
}
