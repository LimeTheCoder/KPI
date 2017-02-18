import javafx.animation.*;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.image.PixelReader;
import javafx.scene.paint.Color;
import javafx.scene.shape.*;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Main extends Application {

    private final static String TRAJECTORY_FILE = "trajectory.bmp";
    private final static double TRANSITION_DURATION = 4000.;
    private final static double ROTATION_ANGLE = 360.;
    private final static double SCALE_TO = 0.5;

    private final Creator computerCreator = new ComputerCreator();

    @Override
    public void start(Stage primaryStage) throws Exception {
        Image image = new Image(TRAJECTORY_FILE);
        ImageView imageView = new ImageView(image);

        Group root = new Group();
        root.getChildren().add(imageView);

        Group computer = computerCreator.create();
        root.getChildren().add(computer);

        Path path = fetchPath(image);

        ParallelTransition parallelTransition = new ParallelTransition();
        parallelTransition.getChildren().addAll(
                createPathTransition(computer, path),
                createRotateTransition(computer),
                createScaleTransition(computer)
        );

        Scene scene = new Scene(root, image.getWidth(), image.getHeight());
        primaryStage.setScene(scene);
        primaryStage.show();

        parallelTransition.play();
    }

    private Path fetchPath(Image image) {
        Path path = new Path();

        int maxHeightIdx = (int)image.getHeight() - 1;
        int maxWidthIdx = (int)image.getWidth() - 1;

        PixelReader pixelReader = image.getPixelReader();

        boolean isFirstPoint = true;

        for(int currY = maxHeightIdx; currY >= 0; currY--) {
            for(int currX = 0; currX <= maxWidthIdx; currX++) {
                if(isBlack(pixelReader.getColor(currX, currY))) {
                    if(isFirstPoint) {
                        path.getElements().add(new MoveTo(currX, currY));
                        isFirstPoint = false;
                    } else {
                        path.getElements().add(new LineTo(currX, currY));
                    }
                    break;
                }
            }
        }

        return path;
    }

    private boolean isBlack(Color color) {
        return color.equals(Color.BLACK);
    }

    private PathTransition createPathTransition(Node node, Path path) {
        PathTransition pathTransition = new PathTransition();

        pathTransition.setDuration(Duration.millis(TRANSITION_DURATION));
        pathTransition.setPath(path);
        pathTransition.setNode(node);
        pathTransition.setCycleCount(Timeline.INDEFINITE);
        pathTransition.setAutoReverse(true);

        return pathTransition;
    }

    private RotateTransition createRotateTransition(Node node) {
        RotateTransition rotateTransition = new RotateTransition(
                Duration.millis(TRANSITION_DURATION),
                node);

        rotateTransition.setByAngle(ROTATION_ANGLE);
        rotateTransition.setCycleCount(Timeline.INDEFINITE);
        rotateTransition.setAutoReverse(true);

        return rotateTransition;
    }

    private ScaleTransition createScaleTransition(Node node) {
        ScaleTransition scaleTransition = new ScaleTransition(
                Duration.millis(TRANSITION_DURATION),
                node);

        scaleTransition.setToX(SCALE_TO);
        scaleTransition.setToY(SCALE_TO);
        scaleTransition.setCycleCount(Timeline.INDEFINITE);
        scaleTransition.setAutoReverse(true);

        return scaleTransition;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
