import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.*;

public class ComputerCreator implements Creator {
    private final static double ARC_VALUE = 10.;

    /** Monitor constants */
    private final static double MONITOR_COORD_X = 44.;
    private final static double MONITOR_COORD_Y = 8.;
    private final static double MONITOR_WIDTH = 80.;
    private final static double MONITOR_HEIGHT = 67.;
    private final static Color MONITOR_COLOR = Color.GRAY;

    /** Face constants */
    private final static double FACE_COORD_X = 54.;
    private final static double FACE_COORD_Y = 18.;
    private final static double FACE_WIDTH = 60.;
    private final static double FACE_HEIGHT = 47.;
    private final static Color FACE_COLOR = Color.rgb(143, 226, 238);

    /** Smile constants */
    private final static double SMILE_CENTER_X = 85.;
    private final static double SMILE_CENTER_Y = 45.;
    private final static double SMILE_RADIUS_X = 23.;
    private final static double SMILE_RADIUS_Y = 15.;
    private final static double SMILE_START_ANGLE = 180.;
    private final static double SMILE_LENGTH = 180.;
    private final static Color SMILE_COLOR = Color.BLACK;

    /** Eye constants */
    private final static double EYE_RADIUS_X = 5.;
    private final static double EYE_RADIUS_Y = 8.;
    private final static double EYE_POINT_RADIUS = 4.;
    private final static Color EYE_COLOR = Color.FLORALWHITE;

    private final static double LEFT_EYE_COORD_X = 75.;
    private final static double LEFT_EYE_COORD_Y = 30.;

    private final static double RIGHT_EYE_COORD_X = 97.;
    private final static double RIGHT_EYE_COORD_Y = 30.;

    /** System block constants */
    private final static double BLOCK_SHIFT = 10.;
    private final static double BLOCK_WIDTH = 100.;
    private final static double BLOCK_HEIGHT = 20.;
    private final static Color BLOCK_COLOR = Color.GRAY;

    /** Power button constants */
    private final static double POWER_BUTTON_RADIUS = 8.;
    private final static Color POWER_BUTTON_COLOR = FACE_COLOR;

    @Override
    public Group create() {
        Group computer = new Group();

        computer.getChildren().add(createMonitor());
        computer.getChildren().add(createFace());
        computer.getChildren().add(createSmile());

        Group leftEye = createEye(LEFT_EYE_COORD_X, LEFT_EYE_COORD_Y);
        computer.getChildren().add(leftEye);

        Group rightEye = createEye(RIGHT_EYE_COORD_X, RIGHT_EYE_COORD_Y);
        computer.getChildren().add(rightEye);

        computer.getChildren().add(createSystemBlock());

        return computer;
    }

    private Rectangle createMonitor() {
        return createRoundedRectangle(MONITOR_COORD_X, MONITOR_COORD_Y,
                MONITOR_WIDTH, MONITOR_HEIGHT, MONITOR_COLOR);
    }

    private Rectangle createFace() {
        return createRoundedRectangle(FACE_COORD_X, FACE_COORD_Y,
                FACE_WIDTH, FACE_HEIGHT, FACE_COLOR);
    }

    private Rectangle createRoundedRectangle(double x, double y, double width,
                                            double height, Color color) {
        Rectangle rectangle = new Rectangle(x, y, width, height);

        rectangle.setArcHeight(ARC_VALUE);
        rectangle.setArcWidth(ARC_VALUE);
        rectangle.setFill(color);

        return rectangle;
    }

    private Arc createSmile() {
        Arc smile = new Arc(SMILE_CENTER_X, SMILE_CENTER_Y,
                SMILE_RADIUS_X, SMILE_RADIUS_Y,
                SMILE_START_ANGLE, SMILE_LENGTH);

        smile.setType(ArcType.OPEN);
        smile.setStroke(SMILE_COLOR);
        smile.setStrokeType(StrokeType.INSIDE);

        return smile;
    }

    private Group createEye(double x, double y) {
        Ellipse ellipse = new Ellipse(x, y, EYE_RADIUS_X, EYE_RADIUS_Y);
        ellipse.setFill(EYE_COLOR);
        Circle circle = new Circle(ellipse.getCenterX(), ellipse.getCenterY(), EYE_POINT_RADIUS);

        Group eye = new Group();
        eye.getChildren().add(ellipse);
        eye.getChildren().add(circle);

        return eye;
    }

    private Group createSystemBlock() {
        double x = MONITOR_COORD_X - BLOCK_SHIFT;
        double y = MONITOR_COORD_Y + MONITOR_HEIGHT;

        Group group = new Group();

        Rectangle block = new Rectangle(x, y, BLOCK_WIDTH, BLOCK_HEIGHT);
        block.setFill(BLOCK_COLOR);
        group.getChildren().add(block);

        Circle powerButton = createPowerButton(block);
        group.getChildren().add(powerButton);

        return group;
    }

    private Circle createPowerButton(Rectangle systemBlock) {
        double x = systemBlock.getX() + systemBlock.getWidth() / 2;
        double y = systemBlock.getY() + systemBlock.getHeight() / 2;

        return new Circle(x, y, POWER_BUTTON_RADIUS, POWER_BUTTON_COLOR);
    }
}
